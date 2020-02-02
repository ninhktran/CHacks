
def get_cat_dict():
    with open('cat.txt') as fd:
        d = {}
        contents = fd.read().split('\n')
        for thing in contents:
            key, value = thing.split(':')
            d[key] = [word.strip() for word in value.split(',')]
    
    return d
