import os
direc = os.path.expanduser("~")
hosts = []
def scanip(ip):
    os.chdir("/home/fastfir/nmap")
    os.system("./nmap -oG " + direc + "/scan.txt -sn -n -T4 " + ip)
    with open('scan.txt', 'r') as scan:
        for line in scan:
            if "Host:" in line:
                ip = line.split(" ", 2)
                hosts.append(ip[1])
    os.system("./nmap -oG " + direc + "/ports.txt -Pn -iL hosts.txt")

