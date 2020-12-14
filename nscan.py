#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome")
print("-----------------------------------------------------")

resp = input("""\nEnter Type Of Scan You Want To Run
                   1)Syn Ack Scan
                   2)Udp Scan
                   3)Thorough Scan\n""")
print("You Selected: ", resp)

ipaddr = input("Enter Ip To Scan: ")
print("You Entered: ", ipaddr)
type(ipaddr)

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ipaddr, '1-1024', '-T4 -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ipaddr].state())
    print(scanner[ipaddr].all_protocols())
    print("Open Ports: ", scanner[ipaddr]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ipaddr, '1-50', '-T5 -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ipaddr].state())
    print(scanner[ipaddr].all_protocols())
    print("Open Ports: ", scanner[ipaddr]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ipaddr, '1-50', '-T2 -A -sS -sC ')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ipaddr].state())
    print(scanner[ipaddr].all_protocols())
    print("Open Ports: ", scanner[ipaddr]['tcp'].keys())
elif resp >= '4':
    print("Invalid Option")
