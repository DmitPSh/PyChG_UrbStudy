

# Не совсем понятен 1-ый позиционный параметр (message), если итоговое
# сообщение формируется по результатам выбора ( оператор if)?

def send_email(message, recipient,*, sender = "university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender:
        message = 'Невозможно отправить письмо с адреса '
        print(f"{message}{sender} на адрес {recipient}.")
        return

    if not (recipient.endswith(".com") or  recipient.endswith(".ru") or  recipient.endswith(".net")):
        message = 'Невозможно отправить письмо с адреса '
        print(f"{message}{sender} на адрес {recipient}.")
        return
    if not (sender.endswith(".com") or  sender.endswith(".ru") or  sender.endswith(".net")):
        message = 'Невозможно отправить письмо с адреса '
        print(f"{message}{sender} на адрес {recipient}.")
        return
    if sender == recipient:
        message = "Нельзя отправить письмо самому себе!"
        print(message)
        return
    if sender == "university.help@gmail.com":
        message = 'Письмо успешно отправлено с адреса '
        print(f"{message} {sender} на адрес {recipient}.")
        return
    else:
        message = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса '
        print(f"{message} {sender} на адрес {recipient}.")

message = " "
recipient = 'vasyok1337@gmail.com'
sender = 'university.help@gmail.com'
send_email(message, recipient)

message = " "
recipient = 'urban.fan@mail.ru'
sender = 'urban.info@gmail.com'
send_email(message, recipient, sender = sender)


message = " "
recipient = 'urban.student@mail.ru'
sender = 'urban.teacher@mail.uk'
send_email(message, recipient, sender = sender)


message = " "
recipient = 'urban.fan@mail.ru'
sender = 'urban.fan@mail.ru'
send_email(message, recipient, sender = sender)
