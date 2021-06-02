import os
import sys
import socket
import matplotlib.pyplot as plt
import dpkt
from dpkt.tcp import TCP

#filename = "NetworkCapture1.pcap"
#address = "192.168.56.1"
#address = ()
#f = ()
#pcap = ()
#numbers_list = ()

numbers_list = []
portnumber_list = []

def find_port (filename, address): 
        # f = open(filename, address ,"r")
        f = open(filename, "rb") 
        pcap = dpkt.pcap.Reader(f)

        for ts, buf in pcap:
               eth = dpkt.ethernet.Ethernet(buf)
               ip = eth.data
               
               if type(ip.data) == TCP : 
                       tcp = ip.data
                       original_ip = socket.inet_ntoa(ip.src)
                       
                       print(original_ip)

               if original_ip == address:
                        numbers_list.append(ts)
                        portnumber_list.append(tcp.dport)
               
        f.close()
        return (numbers_list, portnumber_list)


def plot_graph (numbers_list, portnumber_list):
        plt.plot (numbers_list, portnumber_list, 'b-')
        plt.title ('14501181')
        plt.xlabel ('time stamp')
        plt.ylabel ('Port Number')
        plt.show ()
def main (filename, address): 
        numbers_list, portnumber_list = find_port (filename, address)
        plot_graph (numbers_list, portnumber_list)


main (sys.argv[1], sys.argv[2]) 
#main('NetworkCapture1.pcap','192.168.56.1')
                    