import re
file=open("/home/hazkaz/venv/aoc/input1","r")
data=file.read()
numbers=re.findall('\d',data)
digits=[]
for digit in numbers:
	digits.append(int(digit))

sum=0
for i,digit in enumerate(digits):
	if(digit==digits[(i+1)%len(digits)]):
		sum+=digit
print(sum)

sum=0
for i,digit in enumerate(digits):
	if(digit==digits[(i+int(len(digits)/2))%len(digits)]):
		sum+=digit
print(sum)
