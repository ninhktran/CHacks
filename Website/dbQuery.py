from Website.models import Agency, Subscriber

def check_valid_email(email):
    agency = Agency.query.filter_by(email=email).first()
    if agency:
        return True
    else:
        return False

def get_interested_subs(areas,topics):
    pass

# print(check_valid_email("bigbrother@gmail.com"))
# get_interested_subs(['everett'],['weather'])

# possible email agency addresses listserv@civicplus.com