tshark -r f.pcap -Tfields -e udp.srcport > ans.txt
# r is pcap/pcapng file
# -T type is fields
# -e specified fields