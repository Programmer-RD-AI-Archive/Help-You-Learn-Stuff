import base64
import smtplib

from API import *


class Help_Funcs:
    def send_email(subject: str, message: str, reviver: str) -> bool:
        """
        Send Email using ttest
        """
        gmail_user = config["Configs"]["Gmail"]
        gmail_password = config["Configs"]["Gmail Password"]
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, reviver, message)
            server.close()
            return True
        except:
            return False

    def table_exists_or_not(self, table_name: str, query: str) -> bool:
        try:
            asql = Azure_SQL()
            tables = asql.get_tables()
            if table_name not in tables:
                asql.create_new_table(query)
            return True
        except:
            return False


class Encryption:
    def __init__(self,
                 message: str,
                 encoder: str = config["Configs"]["Encoder Type"]) -> None:
        self.message = message
        self.encoder = encoder

    def encode(self) -> bytes:
        """
        Encode string for privacy and encryption.
        """
        msg_bytes = self.message.encode(self.encoder)
        string_bytes = base64.b64encode(msg_bytes)
        string = string_bytes.decode(self.encoder)
        return string

    def decode(self) -> bytes:
        """
        Decode string for privacy and encryption.
        """
        msg_bytes = self.message.encode(self.encoder)
        string_bytes = base64.b64decode(msg_bytes)
        string = string_bytes.decode(self.encoder)
        return string
