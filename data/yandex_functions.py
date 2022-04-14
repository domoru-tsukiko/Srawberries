import smtplib


def send_notification(email):
    server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
    server.login('', '')
    for to_item in email:
        msg = 'From: %s\r\nTo: %s\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: %s\r\n\r\n' % ('', to_item, 'Тема сообщения')
        msg += 'Текст сообщения'
        server.sendmail('', to_item, msg.encode('utf8'))
    server.quit()


send_notification([''])
