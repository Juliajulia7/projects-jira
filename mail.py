import random
import smtplib


class Emaill(object):

    def __init__(self, address, password):
        self.address = address
        self.password=password

    def passw(self):
        chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        number = int(1)
        length = int(8)
        for n in range(number):
            password = ''
            for i in range(length):
                password += random.choice(chars)
            return password

    def reg(self, toAddr, gen_pass):
        if toAddr.find("")==-1:
            return "badaddress"
        HOST = "smtp.yandex.ru"
        SUBJECT = ""
        FROM = self.address
        BODY = "\r\n".join((
            "From: %s" % FROM,
            "To: %s" % toAddr,
            "Subject: %s" % SUBJECT,
            "",
            gen_pass
        ))

        try:
            server = smtplib.SMTP_SSL(HOST, 465)
            server.login(self.address, self.password)
            server.sendmail(FROM, [toAddr], BODY)
            server.quit()
            return 'Message is sent'
        except smtplib.SMTPRecipientsRefused:
            return 'Invalid addr'
        except UnicodeEncodeError:
            return 'Invalid addr'