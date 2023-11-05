import smtplib, ssl


def contact_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "Write your email or username here"
    password = "Write Your Password here"

    reciever = "aadharkaushik37@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)
