import logging

class ApplicationFirewall:
    def __init__(self, config):
        self.blocked_ips = config.get("defense_config", {}).get("firewall", {}).get("blocked_ips", [])
        self.connection_counts = {}

    def is_allowed(self, ip_address):
        if ip_address in self.blocked_ips:
            logging.warning(f"FIREWALL BLOCK: Dropped connection from blacklisted IP {ip_address}")
            return False
            
        # Basic rate limiting logic could go here
        logging.info(f"FIREWALL ALLOW: Passed connection from {ip_address} to honeypots")
        return True
