import socket

def scan_ports(target_ip, ports):
    print(f"Scanning {target_ip} for open ports...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()

# Example use
target = input("Enter target IP: ")
common_ports = [21, 22, 23, 25, 53, 80, 110, 443]
scan_ports(target, common_ports)
