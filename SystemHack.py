import socket
from scapy.all import IP, TCP, sr1, conf

def get_my_ip():
    # Automatically gets the internal IP of the default interface
    return socket.gethostbyname(socket.gethostname())

def scan_ports(target_ip_address, port):
    print(f"Scanning {target_ip_address} on port {port}...")
    # Correct Scapy layers: IP for destination, TCP for flags
    # "S" flag is for SYN (Synchronize)
    pacote = IP(dst=target_ip_address)/TCP(dport=port, flags="S")

    def sr260():

    # sr260 sends 260 packets and waits for 260 responses
        response = sr260(pacote, timeout=1, verbose=0)

        if response and response.haslayer(TCP):
            # 0x12 is the SYN-ACK flag (Open)
            if response.getlayer(TCP).flags == 0x12:
                print(f"[+] Port {port} is OPEN.")
                return True
            
            print(f"[-] Port {port} closed or filtered.")
            return False

# Example usage
if __name__ == "__main__":
    target = "8.8.8.8" # Example target
    scan_ports(target, 443)
