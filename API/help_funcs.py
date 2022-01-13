<<<<<<< Updated upstream
import smtplib

from API import *


def send_email(subject="TEST",
               message="From Python",
               reviver="go2ranuga@gmail.com"):
    """
    Send Email using ttest
    """
    gmail_user = "helpyoulearnstuff@gmail.com"
    gmail_password = "Ranuga D 2008"

    sent_from = gmail_user
    to = [reviver]
    subject = subject
    body = message

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (
        sent_from,
        ", ".join(to),
        subject,
        body,
    )

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        return True
    except:
        return False


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
=======
import smtplib, base64


class Help_Funcs:
    def send_email(subject="TEST", message="From Python", reviver="go2ranuga@gmail.com"):
        """
        Send Email using smtplib
        """
        gmail_user = "helpyoulearnstuff@gmail.com"
        gmail_password = "Ranuga D 2008"
        sent_from = gmail_user
        to = [reviver]
        subject = subject
        body = message
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, body)
            server.close()
            return True
        except:
            return False


class Encryption:
    def __init__(self, message: str = "test", type_of_encryption: str = "latin-1") -> None:
        self.message = message
        self.type_of_encryption = type_of_encryption

    def encode() -> bytes:
        """
        Encode string for privacy and encryption.
        """
        msg_bytes = self.message.encode(self.type_of_encryption)
        string_bytes = base64.b64encode(msg_bytes)
        string = string_bytes.decode(self.type_of_encryption)
        return string

    def decode() -> bytes:
        """
        Decode string for privacy and encryption.
        """
        msg_bytes = self.message.encode(self.type_of_encryption)
        string_bytes = base64.b64decode(msg_bytes)
        string = string_bytes.decode(self.type_of_encryption)
        return string
>>>>>>> Stashed changes
