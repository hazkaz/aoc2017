import re
import time
file=open("/home/hazkaz/Downloads/input7")
data=file.read()
lines=data.split('\n')[:-1]
dictionary={}
def main():
	
	for line in lines:
		datum=re.split('\W+',line)
		if(datum[2]==''):
			datum=datum[:-1]
		datum=datum[2:]
		for dite in datum:
			if dite in dictionary:
				dictionary[dite]=dictionary[dite]+1
			else:
				dictionary[dite]=1

	for line in lines:
		datum=line.split()[0]
		if datum not in dictionary:
			print(datum)

if __name__ == '__main__':
	main()