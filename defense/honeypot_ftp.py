import socket
from defense.firewall import ApplicationFirewall

def start_ftp_honeypot(config):
    port = config["defense_config"]["honeypots"]["ftp_port"]
    firewall = ApplicationFirewall(config)
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"FTP Honeypot listening on port {port}...")

    while True:
        client, addr = server.accept()
        if firewall.is_allowed(addr[0]):
            client.send(b"220 (vsFTPd 3.0.3)\r\n")
            data = client.recv(1024)
            print(f"[FTP HONEYPOT] Command from {addr[0]}: {data.decode('utf-8', errors='ignore').strip()}")
            client.send(b"331 Please specify the password.\r\n")
        client.close()
