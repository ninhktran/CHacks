from Website.sending import MessageSender
from Website.recieveemail import MessageReciever
from Website.find_sub import get_meta_data
from Website.dbQuery import check_valid_email, get_interested_subs

class EmailForwarder:
    def __init__(self):
        self.main()


    def main(self):
        MessageReciever()
        to, frm, subject = get_meta_data()
        if check_valid_email(frm):


