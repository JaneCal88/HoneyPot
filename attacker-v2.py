import socket
import time

# Target localhost
TARGET_IP = '127.0.0.1'

# Ports to attack
TARGET_PORTS = [21, 22, 80]

# Example payloads provided by ChatGPT
# Sends "admin" "root" access attempts and others
payloads = [
    "admin\n",
    "root\n",
    "GET / HTTP/1.1\nHost: localhost\n",
    "exploit_attempt_xyz\n"
]

# Function to attack the honeypot takes no params
# Sends sample payloads to all target ports on the IP
def attack_honeypot():
    print(f"[+] Starting multi-port attack on {TARGET_IP}")
    for port in TARGET_PORTS:
        print(f"[>>] Attacking port {port}")
        for payload in payloads:
            #try to ensure socket errors close gracefully
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((TARGET_IP, port))
                    print(f"    [>] Sending to port {port}: {payload.strip()}")
                    s.sendall(payload.encode())
                    time.sleep(0.5)
            # errors
            except ConnectionRefusedError:
                print(f"    [!] Connection refused on port {port}")
            except Exception as e:
                print(f"    [!] Error on port {port}: {e}")
        print()

if __name__ == "__main__":
    attack_honeypot()
