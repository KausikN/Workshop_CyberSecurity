'''
IPTables
 - sudo iptables -L : Lists IP Chains - determines which source and destinations to accept packets from
 - sudo iptables -F : Clears IP Tables

XMas Packets
 - All flags are set to 1 in Header of packets (SYN, PSH, URG, FIN, etc)
 - These packets are used as a method of fingerprinting, i.e. finding what protocol is used / nature of TCP IP Stack
 - sudo iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP : Whatever packets coming as input with all flags set shud be dropped - to safeguard against XMas Packets

Null Packets
 - Can crash some servers
 - Used to scan server's ports before a large scale attack
 - sudo iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP : Whatever packets coming as input with all flags 0 shud be dropped - to safeguard against null Packets

SYN Flood Packets
 - SYN bit set to 1 Packet is sent again and again large number of times from different IPs - SPAMS SYN
 - Server allocates storage for each of those connections causing hanging and memory crashes and server crash
 - sudo ipatbles -A INPUT -p tcp ! --syn -m state --state NEW - j DROP

Ports
 - 80/tcp : HTTP
 - 53/udp : DNS
 - 443/tcp : HTTPS
 - 22/tcp : SSH
 - 993/tcp&udp : IMAP
 - 465/tcp : SMTP
'''