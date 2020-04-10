import timeit

setup = '''
def rotate_vect(vect, k=1):
    return [vect[(i - k) % len(vect)] for i in range(len(vect))]


start_letter = 97
end_letter = 113
start = list(range(start_letter, end_letter))
moves_list = None
ords = dict((chr(i), i) for i in range(start_letter, end_letter))
chrs = dict((i, chr(i)) for i in range(start_letter, end_letter))

def dance(moves, repeat=1):
    start_point = 0
    length = len(start)
    pos_dict = dict([(chr(i + 97), i) for i in range(16)])
    for i in range(repeat):
        for move in moves:
            if move[0] == 's':
                spin_count = int(move[1:])
                start_point = (start_point - spin_count) % length
            elif move[0] == 'x':
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

            # elif move[0] == 'p':
            #     a = ords[move[1]]
            #     b = ords[move[3]]
            #     a_pos = pos_dict[move[1]]
            #     b_pos = pos_dict[move[3]]
            #     pos_dict[chrs[a]] = b_pos
            #     pos_dict[chrs[b]] = a_pos
            #     start[a_pos], start[b_pos] = start[b_pos], start[a_pos]

                
with open('input16-shrunk.txt') as file:
    moves_list = file.readline().strip().split(',')
'''

run = '''
dance(moves_list)
'''

data = timeit.repeat(run, setup=setup,repeat=3,number=100)
print(data)
# print("".join(chr(val) for val in rotate_vect(start, -start_point)))
