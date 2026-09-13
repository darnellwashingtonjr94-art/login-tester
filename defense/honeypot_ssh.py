import socket
from defense.firewall import ApplicationFirewall

def start_ssh_honeypot(config):
    port = config["defense_config"]["honeypots"]["ssh_port"]
    firewall = ApplicationFirewall(config)
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"SSH Honeypot listening on port {port}...")

    while True:
        client_socket, addr = server.accept()
        ip = addr[0]
        
        if not firewall.is_allowed(ip):
            client_socket.close()
            continue

        try:
            # Send fake SSH banner
            client_socket.send(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.1\r\n")
            # Log whatever the attacker sends next
            data = client_socket.recv(1024)
            print(f"[SSH HONEYPOT] Data from {ip}: {data.decode('utf-8', errors='ignore').strip()}")
        except Exception:
            pass
        finally:
            client_socket.close()
