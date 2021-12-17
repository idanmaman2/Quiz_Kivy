import socket
from dnslib import DNSRecord

forward_addr = ("8.8.8.8", 53) # dns and port standart 
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
qname = "duckgo.com" # query 
q = DNSRecord.question(qname)
client.sendto(bytes(q.pack()), forward_addr)
data, _ = client.recvfrom(1024)# 1024 bytes - standart size of packet after cut ib router called ip fragment 
d = DNSRecord.parse(data)
print("r", str(d.rr))