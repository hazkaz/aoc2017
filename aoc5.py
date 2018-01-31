import time
file=open("input5","r")
lines=[int(line) for line in file]

def part1():
	step=0
	i=0
	while(i>=0 and i<len(lines)):
	     temp=i
	     i=i+lines[i]
	     lines[temp]=lines[temp]+1
	     step=step+1
	print(step)

def part2():
	step=0
	i=0
	while(i>=0 and i<len(lines)):
	     temp=i
	     i=i+lines[i]
	     if(lines[temp]>=3):
	     	lines[temp]=lines[temp]-1	
	     else:
	     	lines[temp]=lines[temp]+1
	     step=step+1
	return step

start=time.time()	
print(part2())
print("---%s seconds---",time.time()-start)