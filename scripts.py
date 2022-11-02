import os
direc = os.path.expanduser("~")
def scanip(ip):
    os.chdir("/home/fastfir/nmap")
    os.system("./nmap -oG " + direc + "/scan.txt -sn -n -T4 " + ip + " |grep 'ip' scan.txt")
    os.system("")
    os.system("./nmap -oG " + direc + "/ports.txt -Pn -iL hosts.txt")

