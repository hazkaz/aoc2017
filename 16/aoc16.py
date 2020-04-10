from collections import Counter

from matplotlib import pyplot as plt


def rotate_vect(vect, k=1):
    return [vect[(i - k) % len(vect)] for i in range(len(vect))]


start_letter = 97
end_letter = 113
ords = dict((chr(i), i) for i in range(start_letter, end_letter))
chrs = dict((i, chr(i)) for i in range(start_letter, end_letter))
moves_list = None


def dance(moves, repeat=1):
    # print(len(moves))
    start = [ord(i) for i in "nlciboghmkedpfja"]  # list(range(start_letter, end_letter))
    start_point = 0
    length = len(start)
    pos_dict = dict([(chr(i + 97), i) for i in range(16)])

    def spin():
        nonlocal start_point
        spin_count = int(move[1:])
        start_point = (start_point - spin_count) % length

    def exchange():
        if move[2] == '/':
            a = (start_point + int(move[1])) % length
            b = (start_point + int(move[3:])) % length
        else:
            a = (start_point + int(move[1:3])) % length
            b = (start_point + int(move[4:])) % length

        first_char = chrs[start[a]]
        second_char = chrs[start[b]]
        pos_dict[first_char], pos_dict[second_char] = pos_dict[second_char], pos_dict[first_char]
        start[a], start[b] = start[b], start[a]

    def partner():
        a = ords[move[1]]
        b = ords[move[3]]
        a_pos = pos_dict[move[1]]
        b_pos = pos_dict[move[3]]
        pos_dict[chrs[a]] = b_pos
        pos_dict[chrs[b]] = a_pos
        start[a_pos], start[b_pos] = start[b_pos], start[a_pos]

    for i in range(repeat):
        for move in moves:
            if move[0] == 's':
                # spin()
                pass
            elif move[0] == 'x':
                exchange()
            elif move[0] == 'p':
                # partner()
                pass

    return "".join(chr(val) for val in rotate_vect(start, -start_point))


# 1 nlciboghjmfdapek
# 10 nlciboghejpdkafm
# 100 nlciboghapmdejkf
# 1000 nlciboghmkedpfja
# 10000 nlciboghkajdfemp

with open('input16-shrunk.txt') as file:
    moves_list = file.readline().strip().split(',')
# final = dance(moves_list, repeat=9999)
# print(final)

stats = [dance(moves_list, repeat=i) for i in range(50)]
c = Counter(stats)
f = [(stat, index) for index, stat in enumerate(stats)]
print(c)
print(f)
print([c[i] for i in stats])
plt.plot([i + 1 for i in range(len(stats))], [c[i] for i in stats])
# print(stats[36])
# print(stats[99])
# print(stats[162])
plt.show()
