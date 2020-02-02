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
