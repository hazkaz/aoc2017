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


def rotate(s: list, count):
    grid_size = len(s)
    new_grid = [row[:] for row in s]
    if grid_size == 2:
        for i in range(count):
            for start, end in grid_2_rotate.items():
                new_grid[end[0]][end[1]] = s[start[0]][start[1]]
            s = [row[:] for row in new_grid]
    if grid_size == 3:
        for i in range(count):
            for start, end in grid_3_rotate.items():
                new_grid[end[0]][end[1]] = s[start[0]][start[1]]
            s = [row[:] for row in new_grid]
    return new_grid


def flip(s: list, orientation):
    grid_size = len(s)
    new_grid = [row[:] for row in s]
    if orientation == 'v':
        if grid_size == 2:
            for start, end in grid_2_v_flip.items():
                new_grid[end[0]][end[1]] = s[start[0]][start[1]]
        if grid_size == 3:
            for start, end in grid_3_v_flip.items():
                new_grid[end[0]][end[1]] = s[start[0]][start[1]]
    elif orientation == 'h':
        if grid_size == 2:
            for start, end in grid_2_h_flip.items():
                new_grid[end[0]][end[1]] = s[start[0]][start[1]]
        if grid_size == 3:
            for start, end in grid_3_h_flip.items():
                new_grid[end[0]][end[1]] = s[start[0]][start[1]]
    elif orientation == 'd':
        for i in range(grid_size):
            for j in range(grid_size):
                new_grid[i][j] = s[j][i]
    return new_grid


def get_subgrid(grid, row_start, row_end, col_start, col_end):
    return [row[col_start:col_end] for row in grid[row_start:row_end]]


def grid_to_string(grid):
    return '/'.join(''.join(row) for row in grid)


def string_to_grid(string: str):
    return [[c for c in row] for row in string.split('/')]


def match_and_transform(subgrid, guidebook):
    stringized_grid = grid_to_string(subgrid)
    enhanced_subgrid = guidebook[stringized_grid]
    return string_to_grid(enhanced_subgrid)


def unite_grids(divided_grid):
    united_grid = []
    if len(divided_grid[0]) == 1:
        return divided_grid[0][0]
    for divided_row in divided_grid:
        for row in range(len(divided_row[0])):
            united_row = []
            for divided_sub_columns in divided_row:
                united_row.extend(divided_sub_columns[row])
            united_grid.append(united_row)
    return united_grid


start_pattern = [
    ['.', '#', '.'],
    ['.', '.', '#'],
    ['#', '#', '#']
]

update_rules = {}
with open('input.txt') as f:
    for line_num, line in enumerate(f):
        rule, outcome = line.strip().split(' => ')
        grid_rule = string_to_grid(rule)
        for i in range(0, 4):
            rotated_grid = rotate(grid_rule, i)
            hflipped_grid = flip(grid_rule, 'h')
            vflipped_grid = flip(grid_rule, 'v')
            dflipped_grid = flip(grid_rule, 'd')
            update_rules[grid_to_string(rotated_grid)] = outcome
            update_rules[grid_to_string(hflipped_grid)] = outcome
            update_rules[grid_to_string(vflipped_grid)] = outcome
            update_rules[grid_to_string(dflipped_grid)] = outcome
            update_rules[grid_to_string(rotate(hflipped_grid, i))] = outcome
            update_rules[grid_to_string(rotate(vflipped_grid, i))] = outcome
            update_rules[grid_to_string(rotate(dflipped_grid, i))] = outcome

print(f'total enhancement rules : {len(update_rules)}')

pattern = start_pattern

for i in range(18):
    grid_size = len(pattern)
    divided_grid = []
    if grid_size % 2 == 0:
        new_pattern = [row[:] for row in pattern]
        for subgrid_row in range(0, grid_size, 2):
            divided_row = []
            for subgrid_col in range(0, grid_size, 2):
                subgrid = get_subgrid(new_pattern, subgrid_row, subgrid_row + 2, subgrid_col, subgrid_col + 2)
                enhanced_subgrid = match_and_transform(subgrid, update_rules)
                divided_row.append(enhanced_subgrid)
            divided_grid.append(divided_row)

    elif grid_size % 3 == 0:
        new_pattern = [row[:] for row in pattern]
        for subgrid_row in range(0, grid_size, 3):
            divided_row = []
            for subgrid_col in range(0, grid_size, 3):
                subgrid = get_subgrid(new_pattern, subgrid_row, subgrid_row + 3, subgrid_col, subgrid_col + 3)
                enhanced_subgrid = match_and_transform(subgrid, update_rules)
                divided_row.append(enhanced_subgrid)
            divided_grid.append(divided_row)
    pattern = unite_grids(divided_grid)

print(sum(1 if c == '#' else 0 for c in grid_to_string(pattern)))
