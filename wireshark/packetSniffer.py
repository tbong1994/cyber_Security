#packet sniffer!!

import socket
import os


def analyze_ethernet_data(data):
	ether_header = struct.unpack("!",data)
	
def main():
	#get anything in ethernet packet.
	#0x0003 == ETH_P_ALL
	sniffer_socket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0003)) #raw socket
	recv_data = sniffer_socket.recv(2048) #2048 bytes.
	analyze_ethernet_data(recv_data)
