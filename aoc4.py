import re
import hashlib
import math

def check1(lines):
	filtered=[]
	count=0
	for line in lines:
		flag=0
		check=set()
		line=line.split(' ')
		for word in line:
			if(word in check):
				flag=1
			else:
				check.add(word)
		if(flag==0):
			filtered.append(line)
			count+=1
	print(len(filtered))
	return filtered

first_26_primes=[]
start=3
first_26_primes.append(2)

while(len(first_26_primes)!=26):
	flag=0
	for i in range(2,math.ceil(math.sqrt(start))+1):
		if(start%i==0):
			flag=1
			break
	if(flag==0):
		first_26_primes.append(start)
	start+=1

def myhash(word):
	hash=1
	for letter in word:
		hash*=first_26_primes[ord(letter)-97]
	return hash

def check2(lines):
	count=0
	largest=0
	for line in lines:
		flag=0
		match=set()
		for word in line:
			hash=myhash(word)
			if(hash>largest):
				largest=hash
			if(hash in match):
				flag=1
				break
			else:
				match.add(hash)
		if(flag==0):
			count+=1
	print(count)
	print(largest)


def main():
	file=open('input4','r')
	data=file.read()
	lines=data.split('\n')[:-1]
	
	filter1=check1(lines)
	#check2(filter1)

if __name__ == '__main__':
	main()