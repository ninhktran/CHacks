from Website.sending import MessageSender
from Website.recieveemail import MessageReciever
from Website.find_sub import get_meta_data
from Website.dbQuery import check_valid_email, get_interested_subs


class EmailForwarder:
    cat_dict = {'Events': ['holiday',
                           'meeting',
                           'date',
                           'board',
                           'commission'],
                'Emergency': ['accident',
                              'breaking',
                              'earthquake',
                              'emergency',
                              'alert',
                              'break',
                              'urgent',
                              'crisis',
                              'disaster',
                              'fatal'],
                'Traffic': ['jam',
                            'late',
                            'busy',
                            'traffic',
                            'crash',
                            'accidents',
                            'construction'],
                'Weather': ['forecast',
                            'rain',
                            'sunny',
                            'blizzard',
                            'breeze',
                            'climate',
                            'wind',
                            'weather',
                            'warm',
                            'storm',
                            'thunder',
                            'snow',
                            'smog',
                            'hail',
                            'fog',
                            'frost']}

    def __init__(self):
        while True:
            self.main()

    def main(self):
        MessageReciever()
        to, frm, subject = get_meta_data()
        if frm:
            print(frm)
            clean_frm = frm.split()[-1]
            clean_frm = clean_frm.split("<")[1]
            clean_frm = clean_frm.split(">")[0]
            subject = str(subject)
            print(to, clean_frm, subject)
            if check_valid_email(clean_frm):
                area, topic = EmailForwarder.get_topic_area(subject)
                addresses = get_interested_subs(area, topic)
                output = ""
                for address in addresses:
                    output += ("citizen kane" + " <" + address + ">\n")
                output = output[:-2]
                print(output)
                with open('contacts', 'w') as f:
                    f.write("")
                with open("contacts", 'a') as f:
                    f.write(output)
                MessageSender()
            else:
                print("that email wasn't a valid gov email")

    @staticmethod
    def get_topic_area(subject):
        lower_sub = subject.lower()
        locations = ['everett', 'lake stevens', 'snohomish county']
        d = EmailForwarder.cat_dict
        matching_loc = []
        matching_topics = []
        for location in locations:
            if location in lower_sub:
                matching_loc.append(location)
        for key in d:
            key_match = False
            values = d[key]
            for val in values:
                if val in subject:
                    key_match = True
            if key_match:
                matching_topics.append(key.lower())
        return matching_loc, matching_topics


if __name__ == "__main__":
    EmailForwarder()
