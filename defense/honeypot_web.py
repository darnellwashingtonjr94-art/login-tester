import socket
from defense.firewall import ApplicationFirewall

def start_web_honeypot(config):
    port = config["defense_config"]["honeypots"]["web_port"]
    firewall = ApplicationFirewall(config)
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", port))
    server.listen(5)
    print(f"Web Honeypot listening on port {port}...")

    while True:
        client, addr = server.accept()
        if firewall.is_allowed(addr[0]):
            request = client.recv(1024).decode('utf-8', errors='ignore')
            print(f"[WEB HONEYPOT] Request from {addr[0]}:\n{request.splitlines()[0]}")
            
            fake_response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n<html><body><h1>Admin Portal</h1><form><input type='text' name='user'/><input type='password' name='pass'/><input type='submit'/></form></body></html>"
            client.send(fake_response.encode('utf-8'))
        client.close()
