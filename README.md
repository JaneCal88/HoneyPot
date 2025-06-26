# HoneyPot
Honeypot & Attacker Simulation

Honeypot Listener — A multi-port honeypot in python that listens for FTP, SSH, HTTP connections and logs intrusion attempts. (honeypot-v2.py)

Attacker Script — A testing script to simulate attacks against the honeypot and send test payloads. (attacker-v2.py)

⚙️ Requirements
Python 3.6+

No external dependencies required.

🚀 Usage
1. Run the Honeypot (in a terminal or in an IDE)
sudo python3 honeypot-v2.py

2. Run the Attacker Script (from another terminal)
python3 attacker-v2.py


📝 Logging
All connection events and payloads are logged to:
honeypot.log

Each log entry includes:
Timestamp
Protocol
Source IP and port
Destination port
Payload data

🔒 Notes
This honeypot is safe for local testing only.
It only binds to 127.0.0.1 and does not expose services externally.
Do not deploy on a public server without proper isolation (e.g., containers, VMs, firewalls).
