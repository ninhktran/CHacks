import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email as e

MY_ADDRESS = 'alphatester721@gmail.com'
PASSWORD = '@Mamamia2'

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


def read_message(filename):
    """
    Returns a String a of the bytes_message
    """

    with open(filename, 'r') as f:
        template_file_content = f.read()
    return template_file_content


def main():
    emails = get_contacts('mycontacts2')  # read contacts
    email_data = read_message('string_message')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)

    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)
    message = e.message_from_string(email_data)
    # For each contact, send the email:
    for email in emails:
        print(email)
        s.sendmail(MY_ADDRESS, email, message.as_string())


    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()







