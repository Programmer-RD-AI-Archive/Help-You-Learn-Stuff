from mailer import Mailer


def send_email(subject="TEST", message="From Python"):
    mail = Mailer(email="helpyoulearnstuff@gmail.com", password="Ranuga D 2008")
    mail.send(receiver="go2ranuga@gmail.com", subject=subject, message=message)
