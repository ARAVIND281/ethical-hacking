import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="enter the interface name to mac address to change")
parser.add_option("-m","--mac",dest="new_mac",help="enter a mac address to change")

(options, arguments)=parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print(f"[+] Changing MAC address for {interface} to {new_mac}")

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
subprocess.call(["ifconfig",interface,"up"])