import sys
from scapy.all import *
from termcolor import colored

clientprobes = set()
def PacketHandler(pkt):
    if pkt.haslayer(Dot11ProbeReq):
        if len(pkt.info) > 0:
            testcase = "{} --- {}".format(pkt.addr2, pkt.info)
            if testcase not in clientprobes:
                clientprobes.add(testcase)
                print ("Mac client nou: {} Nume AP: {}".format(colored(pkt.addr2, "red"), 
                    colored((pkt.info).decode("utf-8"), "green")))

                print ("\n-----------",colored("Tabel utilizatori conectati", "red"),"---------\n")
                counter = 1
                for probe in clientprobes:
                    [client, ssid] = probe.split("---")
                    print("{} MAC Client: {} Nume AP: {}".format(counter, colored(client, "red"), 
                        colored(ssid,"green")))
                    counter = counter + 1

                print("\n----------------------------------------------------\n")
def ClientFinder(interface, noPackets):
    sniff(iface = interface, count = int( noPackets ), prn = PacketHandler)
