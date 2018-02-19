import re
def knot_hash(data):
    length=[ord(l) for l in data]
    extra=[17, 31, 73, 47, 23]
    for val in extra:
        length.append(val)
    LIST_LENGTH=256
    numbers=[]
    for i in range(LIST_LENGTH):
        numbers.append(i)
    skip=0
    start=0
    def shuffle():
        nonlocal skip
        nonlocal start
        for times in length:
            temp=[]
            for i in range(times):
                temp.append(numbers[(start+i)%LIST_LENGTH])
            temp.reverse()
            for i in range(times):
                numbers[(start+i)%LIST_LENGTH]=temp[i]
            start=(start+(times+skip))%LIST_LENGTH
            skip+=1

    for _ in range(64):
        shuffle()

    sparse_hash=[]
    for i,val in enumerate(numbers):
        if(i%16==0):
            sparse_hash.append(val)
        else:
            sparse_hash[i//16]^=val
    for value in sparse_hash:
        knot_hash=''.join('{0:0{1}x}'.format(int(hash),2) for hash in sparse_hash)
    return knot_hash

def main():
    file=open("input10")
    data=file.read()[:-1]
    hash=knot_hash(data)
    print(hash)

if __name__ == '__main__':
    main()
