import imaplib


class MessageReciever:
    @staticmethod
    def check_for_new():
        return MessageReciever.write_msg()

    @staticmethod
    def get_msg():
        email_user = 'alphatester721@gmail.com'
        email_pass = '@Mamamia2'
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login(email_user, email_pass)
        mail.select('INBOX')

        tmp, data = mail.search(None, 'Unseen')
        msgs = []
        msg_nums = data[0]
        print(msg_nums)
        print(len(msg_nums)//2)
        if msg_nums:
            # num is the index of the new message
            num = msg_nums.split()[0]
            tmp, msg_data = mail.fetch(num, '(RFC822)')

            msgs = msg_data[0][1]

            break
        mail.close()
        return msgs

    @staticmethod
    def write_msg():
        msgs = MessageReciever.get_msg()
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
    MessageReciever()
