import socket
from scapy.all import *
from termcolor import colored

hidden_ssid_aps = set()

def PacketHandler(pkt):
    if pkt.haslayer(Dot11Beacon):
        if not pkt.info:
            if pkt.addr3 not in hidden_ssid_aps:
                hidden_ssid_aps.add(pkt.addr3)
                print("Mac Acces Point ascuns: {}".format(colored(pkt.addr3, "green")))
    elif pkt.haslayer(Dot11ProbeResp) and (pkt.addr3 in hidden_ssid_aps):
        print("Nume AP Ascuns: {} cu adresa MAC: {}".format(colored((pkt.info).decode("utf-8"), "red"), colored(pkt.addr3, "green")))

def HiddenApDiscover(interface, noPackets):
	sniff(iface = interface, count = int( noPackets ), prn = PacketHandler)
