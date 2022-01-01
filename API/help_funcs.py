import smtplib, ssl


def send_email(subject="TEST", message="From Python"):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "helpyoulearnstuff@gmail.com"  # Enter your address
    receiver_email = "go2ranuga@gmail.com"  # Enter receiver address
    password = "Ranuga D 2008"
    message = """\
    Subject: Hi there
    
    This message is sent from Python."""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)





