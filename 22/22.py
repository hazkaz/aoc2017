"""
BEWARE: conventional x and y coordinates swapped.
"""
import cProfile


def turn(curr_dir, turn_direction):
    if turn_direction == 1:
        curr_dir[0], curr_dir[1] = -1 * curr_dir[1], curr_dir[0]
    elif turn_direction == 2:
        curr_dir[0], curr_dir[1] = curr_dir[1], -1 * curr_dir[0]
    elif turn_direction == 3:
        curr_dir[0], curr_dir[1] = -1 * curr_dir[0], -1 * curr_dir[1]
    return curr_dir


infections = set()
weakened = set()
flagged = set()


def read_records():
    with open('input.txt') as f:
        for x, line in enumerate(f):
            for y, c in enumerate(line):
                if c == '#':
                    infections.add((-x, y))
    return x, y


def main():
    x, y = read_records()

    x_start = -x // 2
    y_start = y // 2

    current_direction = [1, 0]
    infect_count = 0
    current_position_tuple = (x_start,y_start)
    for i in range(10000000):

        if current_position_tuple in infections:
            current_direction[0], current_direction[1] = -1 * current_direction[1], current_direction[0]
            infections.remove(current_position_tuple)
            flagged.add(current_position_tuple)

        elif current_position_tuple in weakened:
            weakened.remove(current_position_tuple)
            infections.add(current_position_tuple)
            infect_count += 1

        elif current_position_tuple in flagged:
            current_direction[0], current_direction[1] = -1 * current_direction[0], -1 * current_direction[1]
            flagged.remove(current_position_tuple)

        else:
            current_direction[0], current_direction[1] = current_direction[1], -1 * current_direction[0]
            weakened.add(current_position_tuple)

        current_position_tuple = (
            current_position_tuple[0] + current_direction[0], current_position_tuple[1] + current_direction[1])
    print(infect_count)


if __name__ == "__main__":
    main()
