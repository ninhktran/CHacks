def get_msg():
    with open('testing', 'r') as f:
        contents = str(f.read())
    return contents

def find_sub():
    msg = get_msg()
    thingy = msg.find("Subject: Millions of dollars in Earned Income Tax Credits go unclaimed each")
    start_pos = msg.find("\nSubject:")
    end_pos = msg.find("\nTo:")

    print(start_pos,end_pos)
    return msg[thingy: thingy+150]





print(find_sub())