import re
import time
file=open("/home/hazkaz/Downloads/input8")
data=file.read()
lines=data.split('\n')[:-1]
for index,line in enumerate(lines):
	lines[index]=re.split('\s+',line)
dictionary={}


def main():
	value=None
	for line in lines:
		if line[0] not in dictionary:
			dictionary[line[0]]=0
		if line[4] not in dictionary:
			dictionary[line[4]]=0
		value=eval(str(dictionary[line[4]])+line[5]+line[6])
		print(value)
		if(value):
			if(line[1]=='dec'):
				dictionary[line[0]]=dictionary[line[0]]-int(line[2])
			else:
				dictionary[line[0]]=dictionary[line[0]]+int(line[2])

if __name__ == '__main__':
	main()