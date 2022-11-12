import os
import xml.etree.ElementTree as et
direc = os.path.expanduser("~")
print("This first scan could take a while, be prepared.")
os.chdir(direc + "/nmap")
os.system("./nmap -oX " + direc + "/nmap/ports.xml -A -Pn --open --reason " + ip)
os.system("./nmap --script dns-script.ns " + ip)
os.system("sudo ./nmap --traceroute --script traceroute-geolocation.nse " + ip)
if ("443" or "80" in goodports):
    os.system("./nmap --script http-enum " + ip)
if ("22" in goodports):
    os.system("./nmap --script ssl- " + ip)
    os.system("./nmap --script ssh-auth-methods " + ip)
if ("445" in goodports):
    os.system("./nmap --script smb-vuln- " + ip)
    os.system("./nmap --script smb-os-discovery " + ip)
    os.system("./nmap --script smb-brute " + ip)
    os.system("./nmap --script smb-enum-users " + ip)
            

