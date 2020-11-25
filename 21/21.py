grid_2_rotate = {
    (0, 0): (0, 1),
    (1, 0): (0, 0),
    (0, 1): (1, 1),
    (1, 1): (1, 0)
}

grid_2_h_flip = {
    (0, 0): (0, 1),
    (0, 1): (0, 0),
    (1, 0): (1, 1),
    (1, 1): (1, 0)
}

grid_2_v_flip = {
    (0, 0): (1, 0),
    (1, 0): (0, 0),
    (0, 1): (1, 1),
    (1, 1): (0, 1)
}

grid_3_rotate = {
    (0, 0): (0, 2),
    (0, 1): (1, 2),
    (0, 2): (2, 2),
    (1, 0): (0, 1),
    (1, 2): (2, 1),
    (2, 0): (0, 0),
    (2, 1): (1, 0),
    (2, 2): (2, 0),
    (1, 1): (1, 1)
}

grid_3_h_flip = {
    (0, 0): (0, 2),
    (0, 2): (0, 0),

    (0, 1): (0, 1),
    (1, 1): (1, 1),
    (2, 1): (2, 1),

    (1, 0): (1, 2),
    (1, 2): (1, 0),

    (2, 0): (2, 2),
    (2, 2): (2, 0),
}

grid_3_v_flip = {
    (0, 0): (2, 0),
    (2, 0): (0, 0),

    (1, 0): (1, 0),
    (1, 1): (1, 1),
    (1, 2): (1, 2),

    (0, 2): (2, 2),
    (2, 2): (0, 2),

    (0, 1): (2, 1),
    (2, 1): (0, 1),
}


def rotate(s: str, count):
    grid_size = sum(1 if c == '/' else 0 for c in s) + 1
    new_string = s
    if grid_size == 2:
        for i in range(count):
            for start, end in grid_2_rotate.items():
                new_string = new_string[:end[0] * 3 + end[1]] + s[start[0] * 3 + start[1]] + new_string[
                                                                                             end[0] * 3 + end[1] + 1:]
            s = new_string
    if grid_size == 3:
        for i in range(count):
            for start, end in grid_3_rotate.items():
                new_string = new_string[:end[0] * 4 + end[1]] + s[start[0] * 4 + start[1]] + new_string[
                                                                                             end[0] * 4 + end[1] + 1:]
            s = new_string
    return new_string


def flip(s: str, orientation):
    grid_size = sum(1 if c == '/' else 0 for c in s) + 1
    new_string = s
    if orientation == 'v':
        if grid_size == 2:
            for start, end in grid_2_v_flip.items():
                new_string = new_string[:end[0] * 3 + end[1]] \
                             + s[start[0] * 3 + start[1]] \
                             + new_string[end[0] * 3 + end[1] + 1:]
        if grid_size == 3:
            for start, end in grid_3_v_flip.items():
                new_string = new_string[:end[0] * 4 + end[1]] \
                             + s[start[0] * 4 + start[1]] \
                             + new_string[end[0] * 4 + end[1] + 1:]
    if orientation == 'h':
        if grid_size == 2:
            for start, end in grid_2_h_flip.items():
                new_string = new_string[:end[0] * 3 + end[1]] \
                             + s[start[0] * 3 + start[1]] \
                             + new_string[end[0] * 3 + end[1] + 1:]
        if grid_size == 3:
            for start, end in grid_3_h_flip.items():
                new_string = new_string[:end[0] * 4 + end[1]] \
                             + s[start[0] * 4 + start[1]] \
                             + new_string[end[0] * 4 + end[1] + 1:]

    return new_string


# start_pattern = [
#     ['.','#','.','#','.'''./..#/###]

update_rules = {}
with open('input.txt') as f:
    for line_num, line in enumerate(f):
        rule, outcome = line.strip().split(' => ')
        for i in range(1, 3):
            update_rules[rotate(rule, i)] = outcome
        update_rules[flip(rule, 'v')] = outcome
        update_rules[flip(rule, 'h')] = outcome
print(f'total enhancement rules : {len(update_rules)}')

pattern = start_pattern
for i in range(5):
    grid_size = sum(1 if c == '/' else 0 for c in pattern) + 1
    if grid_size%2==0:

