import socket
import threading
from datetime import datetime

# Set up prior to Main and functions
PORTS = [21, 22, 80]  # FTP, SSH, HTTP
LOG_FILE = 'honeypot.log' #Log file saves to the location of the scripts
BIND_IP = '127.0.0.1'     # Localhost only


# log_event is a function called by the listener function
# It requires the ip, port, and payload of a packet
# and prints this information along with a timestamp.
# It also adds the information to a file, which can be updated above
def log_event(ip, port, payload):
    timestamp = datetime.now().isoformat()
    message = f"[{timestamp}] {ip}:{port} -> {payload}"
    print(message)
    with open(LOG_FILE, 'a') as log:
        log.write(message + '\n')

# listener is a function that is called by the main function
# It attempts to gracefully create, bind and listen to a socket
# for one port which is given as the parameter. If successful,
# the function attempts to decode any data given in the traffic
def listener(port):
    # using "with" for graceful exit of socket when creating
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((BIND_IP, port))
        s.listen(5)
        print(f"[+] Listening for traffic on {BIND_IP}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                ip, src_port = addr
                try:
                    data = conn.recv(1024).decode(errors='ignore').strip()
                    if not data:
                        data = "<no data>"
                    log_event( ip, port, data)
                except Exception as e:
                    print(f"[!] Error on port {port}: {e}")


# Main function
# Main function uses threading. This was a suggestion by ChatGPT
# to allow the function to listen to all ports at the same time.
# The function creates a thread for each port, then keeps the threads
# listening until the user presses a key.
def start_honeypot():
    print("[*] Honeypot is starting on localhost...")

    # Start listeners
    for port in PORTS:
        t = threading.Thread(target=listener, args=(port,), daemon=True)
        t.start()

    # Keep main thread alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\n[!] Honeypot stopped by user.")

if __name__ == "__main__":
    start_honeypot()
