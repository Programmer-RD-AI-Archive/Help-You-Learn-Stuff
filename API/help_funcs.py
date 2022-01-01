from API import *
import base64


def send_email(subject="TEST", message="From Python"):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "helpyoulearnstuff@gmail.com"  # Enter your address
    receiver_email = "go2ranuga@gmail.com"  # Enter receiver address
    password = "Ranuga D 2008"
    message = f"""\
    Subject: {subject}
    
    {message}"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def encode(message: str) -> bytes:
    """
    Encode string for privacy and encryption.
    """
    msg_bytes = message.encode("latin-1")
    string_bytes = base64.b64encode(msg_bytes)
    string = string_bytes.decode("latin-1")
    return string


def decode(message: str) -> bytes:
    """
    Decode string for privacy and encryption.
    """
    msg_bytes = message.encode("latin-1")
    string_bytes = base64.b64decode(msg_bytes)
    string = string_bytes.decode("latin-1")
    return string
