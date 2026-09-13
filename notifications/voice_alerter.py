from twilio.rest import Client

def trigger_voicemail_alert(config):
    twilio_cfg = config["twilio"]
    client = Client(twilio_cfg["account_sid"], twilio_cfg["auth_token"])
    
    # TwiML instructions read out by text-to-speech when answered or sent to voicemail
    twiml_response = '<Response><Say>Security alert. Valid credentials have been detected and logged.</Say></Response>'
    
    client.calls.create(
        twiml=twiml_response,
        to=twilio_cfg["to_number"],
        from_=twilio_cfg["from_number"]
    )
