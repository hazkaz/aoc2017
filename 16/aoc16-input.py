moves_list = None
with open('input16.txt') as file:
    moves_list = file.readline().strip().split(',')

length = 16
spin_counter = 0
updated_moves_list = []
rearrange_spin = list(range(16))

for move in moves_list:
    if move[0] == 's':
        spin_counter = (spin_counter + int(move[1:])) % length
    elif move[0] == 'x':
        a, b = list(map(lambda x: (int(x) - spin_counter) % length, move[1:].split('/')))
        rearrange_spin[a], rearrange_spin[b] = rearrange_spin[b], rearrange_spin[a]

    elif move[0] == 'p':
        # updated_moves_list.append(move)
        pass

rearrange_list = []
for i in range(len(rearrange_spin) - 1):
    for j in range(i + 1, len(rearrange_spin)):
        if rearrange_spin[j] < rearrange_spin[i]:
            rearrange_list.append(f"x{i}/{j}")
            rearrange_spin[i], rearrange_spin[j] = rearrange_spin[j], rearrange_spin[i]

updated_moves_list.extend(reversed(rearrange_list))

updated_moves_list.append(f"s{spin_counter}")

with open('input16-shrunk.txt', 'w') as file:
    file.write(",".join(updated_moves_list))
print("done writing to file")
