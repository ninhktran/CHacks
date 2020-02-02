from Website.models import Agency, Subscriber

def check_valid_email(email):
    agency = Agency.query.filter_by(email=email).first()
    if agency:
        return True
    else:
        return False

def get_interested_subs(area,topic):
    subscribers = Subscriber.query.all()
    print(subscribers)
    matched_adds = []
    for sub in subscribers:
        topic_match = False
        area_match = False
        for a in area:
            if a in sub.area.split(','):
                # print('area match')
                area_match = True
        for t in topic:
            if t in sub.topic.split(','):
                # print('topic match')
                topic_match = True
        if area_match and topic_match:
            matched_adds.append(sub.email)



    print(matched_adds)
    return matched_adds

# print(check_valid_email("bigbrother@gmail.com"))
# get_interested_subs(['everett'],['weather'])

# possible email agency addresses listserv@civicplus.com