import os
import xml.etree.ElementTree as et
goodports = []
direc = os.path.expanduser("~")
def scanip(ip):
    print("This first scan could take a while, be prepared.")
    os.chdir(direc + "/nmap")
    os.system("./nmap -oX " + direc + "/nmap/ports.xml -A -Pn --open --reason " + ip)
    ports = et.parse("ports.xml")
    root = ports.getroot()
    for port in root.iter("port"):
        if port.attrib["portid"] not in goodports:
            goodports.append(port.attrib["portid"])
    os.system("sudo ./nmap --traceroute --script traceroute-geolocation.nse " + ip)
    if ("443" or "80" in goodports):
        os.system("./nmap --script http-enum " + ip)
    if ("22" in goodports):
        os.system("./nmap --script ssh-brute " + ip)
        os.system("./nmap --script ssh-auth-methods " + ip)
    if ("445" in goodports):
        os.system("./nmap --script smb-vuln- " + ip)
        os.system("./nmap --script smb-os-discovery " + ip)
        os.system("./nmap --script smb-brute " + ip)
        os.system("./nmap --script smb-enum-users " + ip)
ip = input("Enter the target ip: ")
scanip(ip)
