import smtplib
import email as e


class MessageSender:
    MY_ADDRESS = 'alphatester721@gmail.com'
    PASSWORD = '@Mamamia2'
    CONTACTS = 'contacts'

    def __init__(self):
        self.main()

    def main(self):
        MessageSender.send_message()

    @staticmethod
    def get_contacts(filename):
        """
        Return one list of email addresses
        read from a file specified by filename.
        """
        emails = []
        with open(filename, mode='r', encoding='utf-8') as contacts_file:
            for a_contact in contacts_file.read().split('\n'):
                emails.append(a_contact)
        return emails

    @staticmethod
    def read_message(filename):
        """
        Returns a String a of the bytes_message
        """

        with open(filename, 'r') as f:
            template_file_content = f.read()
        return template_file_content

    @staticmethod
    def send_message():
        emails = MessageSender.get_contacts(MessageSender.CONTACTS)  # read contacts
        email_data = MessageSender.read_message('string_message')

        # set up the SMTP server
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)

        s.starttls()
        s.login(MessageSender.MY_ADDRESS, MessageSender.PASSWORD)
        message = e.message_from_string(email_data)
        # For each contact, send the email:
        for email in emails:
            print(email)
            s.sendmail(MessageSender.MY_ADDRESS, email, message.as_string())


        # Terminate the SMTP session and close the connection
        s.quit()


if __name__ == '__main__':
    MessageSender()
