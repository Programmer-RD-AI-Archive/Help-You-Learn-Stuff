import base64
import requests


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


def verify_email(email_address):
    response = requests.get(
        "https://isitarealemail.com/api/email/validate", params={"email": email_address}
    )

    status = response.json()["status"]
    if status == "valid":
        return True
    elif status == "invalid":
        return False
    else:
        return False
