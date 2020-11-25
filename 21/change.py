import re


def dec_one(match):
    val = int(match.groups()[0])
    return str(val - 1)


with open('a.txt') as f:
    with open('b.txt', 'w') as g:
        for line in f:
            changed_line = re.sub(r'(?<!_)(\d)', dec_one, line)
            g.write(changed_line)
