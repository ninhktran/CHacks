from email.parser import BytesParser
from email.policy import default

def get_meta_data():
    with open('bytes_message', 'rb') as fp:
        headers = BytesParser(policy=default).parse(fp)
    to = headers['to']
    frm = headers['from']
    subject = headers['subject']
    return to, frm, subject
