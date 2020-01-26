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