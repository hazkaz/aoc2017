import re
file=open("/home/hazkaz/venv/aoc/input2",'r')
#data=file.read()
data=file.readline()
lines=[]

while(data):
	line=re.split('\s',data)[:-1]
	for i,l in enumerate(line):
		line[i]=int(l)
	lines.append(line)
	data=file.readline()

checksum=0
for line in lines:
	largest=-1
	smallest=-1
	for num in line:
		if(largest==-1):
			largest=num
		else:
			largest=num if num>largest else largest
		if(smallest==-1):
			smallest=num
		else:
			smallest=num if num<smallest else smallest
	checksum+=(largest-smallest)
print(checksum)

checksum=0
for line in lines:
	largest=-1
	smallest=-1
	for i,num in enumerate(line):
		for j,bum in enumerate(line):
			if(i!=j and num%bum==0):
				checksum+=(num/bum)
print(checksum)