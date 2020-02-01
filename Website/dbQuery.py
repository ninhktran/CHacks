from Website.models import Agency, Subscriber

def check_valid_email(email):
    agency = Agency.query.filter_by(email=email).first()
    if agency:
        return True
    else:
        return False

    passdef get_interested_subs(areas,topics):
