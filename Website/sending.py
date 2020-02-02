import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
    Returns a String a of the message
    """

    with open(filename, 'r') as f:
        template_file_content = f.read()
    return template_file_content


def main():
    emails = get_contacts('mycontacts2')  # read contacts
    message = read_message('message.html')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)

    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    for email in emails:
        print(email)
        msg = MIMEMultipart()  # create a message.html

        # add in the actual person name to the message.html template


        # setup the parameters of the message.html
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "This is TEST from your local Government Agency"
        # msg.attach(message)
        # add in the message.html body
        msg.attach(MIMEText(message, 'html'))

        # send the message.html via the server set up earlier.
        s.send_message(msg)
        del msg

    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()









