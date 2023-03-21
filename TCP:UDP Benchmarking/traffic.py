# Chris Stankus and Ryan Mosenkis

import argparse
import socket
import time
import random

# Parse command line arguments
parser = argparse.ArgumentParser(description='Generate network traffic packets')
parser.add_argument('--protocol', choices=['tcp', 'udp'], default='udp', help='Protocol to use')
parser.add_argument('--size', type=int, default=1024, help='Packet size in bytes')
parser.add_argument('--bandwidth', type=int, default=100, help='Bandwidth in packets per second')
parser.add_argument('--distribution', choices=['burst', 'uniform'], default='uniform', help='Distribution of packets to generate')
parser.add_argument('--duration', type=int, default=10, help='Duration to run in seconds')
args = parser.parse_args()

# Initialize variables
packet_loss = 0
out_of_order_packets = 0
total_packets_sent = 0
packets_sent = 0 
rtt = 0
start_time = time.time()

# Create a socket based on protocol and connect to socket 12345
if args.protocol == 'tcp':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
else:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('134.82.9.147', 12346))

# Generate packets
while (time.time() - start_time) < args.duration:
    total_packets_sent += 1
    packet_data = bytes(random.getrandbits(8) for _ in range(args.size))

    # Send packet in burst mode
    if args.distribution == 'burst':
        send_time = time.time()
        sock.send(packet_data)
        print('Packet sent successfully')
        packets_sent += 1

        time.sleep(1/args.bandwidth - (time.time() - send_time))

    # Send packet in uniform mode
    else:
        send_time = time.time()
        sock.send(packet_data)
        print('Packet sent successfully')
        packets_sent += 1

        send_interval = 1/args.bandwidth - (time.time() - send_time)
        if send_interval > 0:
            time.sleep(send_interval)
    
    # Receive packet to calculate RTT
    response = sock.recv(args.size)
    rtt += time.time() - send_time

# Collect statistics
packet_loss = (total_packets_sent - packets_sent) / total_packets_sent * 100
out_of_order_packets = out_of_order_packets / total_packets_sent * 100
avg_rtt = rtt / total_packets_sent

# Display collected statistics
print('Packet loss rate: {:.2f}%'.format(packet_loss))
print('Out of order packet rate: {:.2f}%'.format(out_of_order_packets))
print('Average RTT: {:.2f} ms'.format(avg_rtt * 1000))
