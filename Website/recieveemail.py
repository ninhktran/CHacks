import imaplib

def get_msg():
    email_user = 'alphatester721@gmail.com'
    email_pass = '@Mamamia2'
    mail = imaplib.IMAP4_SSL("imap.gmail.com",993)
    mail.login(email_user, email_pass)
    mail.select('INBOX')

    tmp, data = mail.search(None, 'Unseen')
    msgs = []
    print(len(data[0].split()))
    for num in data[0].split():
        tmp, data = mail.fetch(num, '(RFC822)')

        msgs.append(data[0][1])

        break
    mail.close()
    return msgs

def write_msg():
    msgs = get_msg()
    # print(msgs)
    with open("bytes_message", 'w') as f:
        f.write("")

    with open("bytes_message", 'ab') as f:
        for m in msgs:
            f.write(m)
    with open("string_message",'w') as f:
        f.write("")
    with open('string_message', 'a') as f:
        for m in msgs:
            f.write(str(m.decode("ASCII")))

if __name__ == "__main__":
    write_msg()
