import re
file=open("/home/hazkaz/venv/aoc/input10")
data=file.read()
values=data.split(',')
length=[]
for l in values:
	length.append(int(l))
LIST_LENGTH=256
#length=[3,4,1,5]
def main():
	numbers=[]
	skip=0
	start=0
	for i in range(LIST_LENGTH):
		numbers.append(i)
	
	for times in length:
		temp=[]
		for i in range(times):
			temp.append(numbers[(start+i)%LIST_LENGTH])
		#print(temp)
		temp.reverse()
		for i in range(times):
			numbers[(start+i)%LIST_LENGTH]=temp[i]
		start=(start+(times+skip))%LIST_LENGTH
		skip+=1
		#print(numbers)
	print(numbers[0]*numbers[1])

if __name__ == '__main__':
	main()