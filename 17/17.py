STEP_SIZE = 376
storm = [0]
i = 0
zero_index = None
num_count = 1
for j in range(1, 50000000+1):
    steps = (i + STEP_SIZE) % num_count + 1
    i = steps
    # storm.insert(i, j)
    # print(storm)
    num_count += 1
    if i == 1:
        zero_index = j

print(zero_index)
# print(storm[i+1])