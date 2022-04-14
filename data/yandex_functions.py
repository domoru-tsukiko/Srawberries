import smtplib


def send_notification(email):
    sender = 'test@yandex.ru'
    sender_password = 'password'
    mail_lib = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    mail_lib.login(sender, sender_password)
    for to_item in email:
        msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' % (sender, to_item, 'Тема сообщения')
        msg += ''
        mail_lib.sendmail(sender, to_item, msg.encode('utf8'))
    mail_lib.quit()
