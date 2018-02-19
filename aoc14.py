from aoc10 import knot_hash
from collections import Counter
def main():
    input='ljoxqyyw'
    open=0
    for i in range(128):
        row_input=input+'-'+str(i)
        hex_repr=knot_hash(row_input)
        binary_repr=bin(int(hex_repr,16))[2:]
#        print(hex_repr)
        used=Counter(binary_repr)['1']
        open+=used
    print(open)
    
if __name__=='__main__':
    main()
