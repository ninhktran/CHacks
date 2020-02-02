import imaplib
import base64
import os
import email

email_user = 'alphatester721@gmail.com'
email_pass = '@Mamamia2'
mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
mail.login(email_user, email_pass)
mail.select('INBOX')
type, data = mail.search(None, 'UNSEEN')
mail_ids = data[0]
id_list = mail_ids.split()
for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    for part in email_message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join('/Users/mateocastanogomez/Documents/readEmail', fileName)
            print('He descargado archivos 🙂')
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
    for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode('utf-8'))
                email_subject = msg['subject']
                email_from = msg['from']
                print ('De : ' + email_from + '\n')
                print ('Asunto : ' + email_subject + '\n')
                while msg.is_multipart():
                    msg = msg.get_payload(0)
                content = msg.get_payload(decode=True)
                print(content)