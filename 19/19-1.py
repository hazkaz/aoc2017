import string

graph = []
start_point = (0, 0)
with open('input.txt') as file:
    for line in file:
        graph.append(line)
for index, char in enumerate(graph[0]):
    if char == '|':
        start_point = (0, index)

print(start_point)


def same_dir(point, direction, g):
    if direction[0] != 0:
        return vertical(point, direction, g)
    else:
        return horizontal(point, direction, g)


def vertical(point, direction, g):
    if direction[0] == 1:
        return (point[0] + 1, point[1]), direction
    else:
        return (point[0] - 1, point[1]), direction


def horizontal(point, direction, g):
    if direction[1] == 1:
        return (point[0], point[1] + 1), direction
    else:
        return (point[0], point[1] - 1), direction


def junction(point, direction, g):
    if direction[1] == 0:
        if g[point[0]][point[1] + 1] != ' ':
            return (point[0], point[1] + 1), (0, 1)
        else:
            return (point[0], point[1] - 1), (0, -1)
    else:
        if g[point[0] + 1][point[1]] != ' ':
            return (point[0] + 1, point[1]), (1, 0)
        else:
            return (point[0] - 1, point[1]), (-1, 0)


choices = {
    '|': same_dir,
    '-': same_dir,
    '+': junction,
}

current_point = start_point
current_direction = (1, 0)
landmarks = []
x_max = len(graph)
y_max = len(graph[0])
counter = 0
while True:
    glyph = graph[current_point[0]][current_point[1]]
    print(glyph)
    try:
        current_point, current_direction = choices[glyph](current_point, current_direction, graph)
        counter += 1
        if current_point[0] < 0 or current_point[0] > x_max or current_point[1] < 0 or current_point[1] > y_max:
            break
    except KeyError:
        if glyph in string.ascii_uppercase:
            landmarks.append(glyph)
            current_point, current_direction = same_dir(current_point, current_direction, graph)
            counter += 1
        elif glyph == ' ':
            break
    print(current_point)
print(''.join(landmarks))
print(counter)
