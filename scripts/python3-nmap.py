import nmap3
from pprint import pprint

ip = "192.168.33.46"

if __name__ == '__main__':
    
    nmap = nmap3.NmapScanTechniques()
    
    results = nmap.nmap_tcp_scan(ip, args="-sV -sC -p-")

    ports=results[ip]["ports"]

    for port in ports:
        print(port["portid"])