import imaplib

def get_msg():
    email_user = 'alphatester721@gmail.com'
    email_pass = '@Mamamia2'
    mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
    mail.login(email_user, email_pass)
    mail.select('INBOX')

    tmp, data = mail.search(None, 'UNSEEN')
    msgs = []
    print(len(data[0].split()))
    for num in data[0].split():
        tmp, data = mail.fetch(num, '(RFC822)')
        # print(data)
        msgs.append(data[0][1].decode('ASCII'))
        # pprint.pprint(data[0][1].decode('ASCII'))
        # pprint.pprint(data[0][1])
    mail.close()
    return msgs

def write_msg():
    msgs = get_msg()
    # print(msgs)
    with open("testing", 'w') as f:
        f.write("")

    with open("testing", 'a') as f:
        for m in msgs:
            f.write(m)

if __name__ == "__main__":
    write_msg()


# type, data = mail.search(None, 'UNSEEN')
#
# mail_ids = [int(num) for num in str(data[0].decode('ASCII')).split()]
# for num in mail_ids:
#     typ, data = mail.fetch(num, '(RFC822)' )
#     raw_email = data[0][1]
#     raw_email_string = raw_email.decode('utf-8')
#     email_message = email.message_from_string(raw_email_string)
#     for part in email_message.walk():
#         if part.get_content_maintype() == 'multipart':
#             continue
#         if part.get('Content-Disposition') is None:
#             continue
#         fileName = part.get_filename()
#         if bool(fileName):
#             filePath = os.path.join('/Users/mateocastanogomez/Documents/readEmail', fileName)
#             print('He descargado archivos 🙂')
#             if not os.path.isfile(filePath) :
#                 fp = open(filePath, 'wb')
#                 fp.write(part.get_payload(decode=True))
#                 fp.close()
#             subject = str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
#     for response_part in data:
#             if isinstance(response_part, tuple):
#                 msg = email.message_from_string(response_part[1].decode('utf-8'))
#                 email_subject = msg['subject']
#                 email_from = msg['from']
#                 print ('De : ' + email_from + '\n')
#                 print ('Asunto : ' + email_subject + '\n')
#                 while msg.is_multipart():
#                     msg = msg.get_payload(0)
#                 content = msg.get_payload(decode=True)
#                 with open("message", "w") as f:
#                     f.write(content)
