import requests

def get_current_ip(config=None):
    try:
        proxies = None
        if config and config.get("proxy", {}).get("enabled"):
            proxies = {
                "http": config["proxy"]["http"],
                "https": config["proxy"]["https"]
            }
        
        response = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=10)
        ip_data = response.json()
        print(f"Current Outbound IP: {ip_data.get('origin')}")
        return ip_data.get('origin')
    except Exception as e:
        print(f"Failed to fetch current IP: {e}")
        return None
