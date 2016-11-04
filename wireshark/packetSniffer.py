#packet sniffer!!

import socket
import os
import struct
import binascii

def analyze_ethernet_data(data):
	ip_bool = False
	#IPv4 = 0x0800
	#sturct.unpack can only take string of size 14. 6s6sH, H=unisigned int=size 2. 6+6+2.
	ether_header = struct.unpack("!6s6sH",data[:14]) #6s means 6bytes for the MAC destination and source.
	
	#MAC addresses are in hex, so convert to hex.
	dest_mac = binascii.hexlify(ether_header[0]) #destination address
	source_mac = binascii.hexlify(ether_header[1]) #source address
	next_proto = ether_header[2] #next protocol. IPv4 or IPv6, etc
	
	print dest_mac
	print source_mac
	print hex(next_proto)
	
	if(hex(next_proto)==0x0800): #IPv4
		ip_bool = True
	
	data = data[14:]
	return data, ip_bool
	
def main():
	#get anything in ethernet packet.
	#0x0003 == ETH_P_ALL
	sniffer_socket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0003)) #raw socket
	recv_data = sniffer_socket.recv(2048) #2048 bytes.
	#analyze_ethernet_data(recv_data)
	data, ip_bool = analyze_ethernet_data(recv_data)
	if(ip_bool): #only care about IPv4
		data = analyze_ethernet_data(data)

main()
