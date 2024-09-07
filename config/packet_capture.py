import scapy.all as scapy
from scapy.all import *

scapy.all.show_interfaces()

def capture_packets(interface, count):
    packets = sniff(iface=interface, count=count)
    return packets

