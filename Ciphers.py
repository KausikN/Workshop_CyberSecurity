'''
Holy Trinity
 - Confidentiality
  -- Encryption : Encryption Cracking
  -- Man in middle attack : A sends to B but C intercepts and without proper authorisation reads or even changes the data
  -- Insider Leaks
 - Integrity
  -- Access Controls - allow access only to proper personnel
  -- Cryptographic Checksums
  -- Uninterrupted power supplies
  -- Backups
 - Availablity
  -- Failover, Redunc=dancy, RAID, Firewalls and Proxy Servers, Disaster recovery plans
  -- Challenges - DDos attacks, Ransomware attacks and disrupting power supply

Encryption
Terms
 - Plaintext : Readable
 - CCiphertext : Result of encryption
 - Encryption : Function that converts plaintext to ciphertext
 - Decryption : Ciphertext to plaintext
Ciphers
 - Caesar cipher : shift all alphabets by some amount - Weak cipher as shift is one of 26 values - can be bruteforced easily
 - Symmetric Key Cryptography : A secret key is used to encrypt and decrypt data - i.e. same key to encrypt and decrypt (eg. Caesar Cipher)
 - S-Box : A Cipher which substitutes each char by some other char
 - P-Box : A Cipher where each position in plaintext is replaced by some other position in same plaintext - i.e. 1st char goes to 2nd char and vice versa, 'ab' -> 'ba'
 - Asymmetric Encyption : Public Key and Private Key - Key A encrypts and Key B Decrypts (RSA)

 HTTPS
  - Encrypts data using SSL
  - Data secured using symmetric key cryptography
  - Identity established using assymetric key encryption

Symmetric Key Encyprions
 - DES : Data Encryption Standard
 - AES : Advanced Encryption Standard

DES
 - Data encrypted by symmetric key
 - Symmetric key encrypted by assymtyeric key cryptography by public key
 - So encrypted key is sent to receiver and he decrypts using private key and gets the symmetric key
 - Using symm key he decrypts data

RSA
 - public key is (n, e)
 - private key is (d)
 - Message is m
 - To encrypt do, pow(m, e) % n
 - Receiver recieves cipher and does
 - pow(Cipher, d)

 - n, e, d are genrated such that ed = 1 mod n, and d = value from 1 to phi(n) where phi(n) = (p-1)(q-1) and n = pq
 - So, Cipher is pow(m, e) % n
 - While decrypting, 
 - pow(pow(m, e), d)
 - pow(m, ed)
 - pow(m, 1) % n
 - m % n
 - Now as n is known, receiver can get back m

 - Eg. Let p = 3, q = 11
 - So, n = pq = 3 x 11 = 33
 - So, phi(n) = (p-1)(q-1) = 2 x 10 = 20
 - Let e = 7 (1 <= e <= phi(n) as 1 <= 7 <= 20)
 - d is such that ed % phi(n) = 1
 - so, d = 3 (As 3 x 7 = 21 % 20 = 1)
 - So, public key is (n, e) -> (33, 7)
 - Suppose message is m = 9
 - Encrypted ciphertext = pow(m, e) % n = pow(9, 7) % 33 = 15
 - Receiver recieves cipher as 15 and public key as (33, 7)
 - private key is (d) = (3)
 - Receiver decrypts by doing pow(cipher, d) % n = pow(15, 3) % 33 = 3375 % 33 = 9 = original message

Hashing
 - We can encrypt but cant decrypt back the data
 - md5, sha3
 - used in passwords
 - Let p1 be original password and it is hashed to get some code
 - So, when user enters some password p2, it is also hashed and its value is compared to p1 hash
 - If same, the passwords match else no
 - But we cant get p1 from hash of p1

'''

# Encryptions

# Caesar Cipher
def CaesarCipher(data, nshift=0, key=''):
    enc = ''
    if key == '':
        for c in data:
            enc += chr(ord(c) + nshift)
    else:
        for c, s in zip(data, key):
            enc += chr(ord(c) + ord(s))
    return enc

# S Box Cipher
def SBoxCipher(data, subsdict):
    enc = ''
    for c in data:
        enc += subsdict[c]
    return enc

# P Box Cipher
def PBoxCipher(data, possubs):
    enc = ''
    for i in range(len(data)):
        enc += data[possubs[i]]
    return enc

print(CaesarCipher('ab', nshift=1))