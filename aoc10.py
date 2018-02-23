import re


def knot_hash(data):
	LIST_LENGTH=256
	length=[ord(l) for l in data]
	extra=[17, 31, 73, 47, 23]
	for val in extra:
		length.append(val)
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
	# for value in sparse_hash:
	# 	print('{0:0{1}x}'.format(int(value),2))
	final_hash=''.join('{:02x}'.format(hash,2) for hash in sparse_hash)
	return final_hash

def main():
	file=open("input10")
	data=file.read()[:-1]
	print(knot_hash(data))

if __name__ == '__main__':
	main()