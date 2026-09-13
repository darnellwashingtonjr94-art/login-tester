import requests

def get_session_with_proxy(config):
    session = requests.Session()
    proxy_cfg = config.get("proxy", {})
    
    if proxy_cfg.get("enabled"):
        session.proxies = {
            "http": proxy_cfg["http"],
            "https": proxy_cfg["https"]
        }
    
    return session
