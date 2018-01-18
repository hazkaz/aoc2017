import math
from time import sleep
number=368078#int(input())
def find(number):
	level=int(math.ceil((math.ceil(math.sqrt(number))+1)/2))
	start=math.pow(((level-1)*2)-1,2)+1
	end=math.pow((level*2)-1,2)

	x=2*level-1
	y=2*level-2
	dir=[0,-1]
	value=start
	print(x,y)

	while(value<number):
		while(dir[0]*x!=-1 and dir[1]*y!=-1 and dir[0]*x!=2*level-1 and dir[1]*y!=2*level-1):
				if(value==number):
					break
				x+=dir[0]
				y+=dir[1]
				value+=1
		dir[0],dir[1]=dir[1]*1,dir[0]*-1
	print(x,y)
	print(abs((2*level-2)/2-x)+abs((2*level-2)/2-y))
#find(number)

number=368078
def construct(number):
	level=2
	x=1
	y=0
	value=2
	dir=[0,1]
	while(value<number):
		
		limit=level-1
		while(dir[1]*y!=limit and dir[0]*x!=limit):
			if(value==number):
				break
			x+=dir[0]
			y+=dir[1]
			value+=1
		

		if(x==limit and y==-limit):
			x+=1
			level+=1
			value+=1
		dir[0],dir[1]=dir[1]*-1,dir[0]*1

	print(abs(x)+abs(y))
#construct(number)

number=368078

def evaluate():
	for things in neighbours:
			#print((x+things[0],y+things[1]))
			if (x+things[0],y+things[1]) in values:
				if((x,y) in values):
					values[(x,y)]+=values[(x+things[0],y+things[1])]
				else:
					values[(x,y)]=values[(x+things[0],y+things[1])]

level=2
x=1
y=0
value=2
values={(0,0):1}
dir=[0,1]
flag=0
neighbours=set([(1,1),(-1,-1),(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)])
while(value<number):

	limit=level-1
	while(dir[1]*y!=limit and dir[0]*x!=limit):
		evaluate()
		if(values[(x,y)]>number):
			flag=1
			break
		value+=1
		x+=dir[0]
		y+=dir[1]
		#print(values)
		#sleep(0.1)

	if(x==limit and y==-limit):
		evaluate()
		if(values[(x,y)]>number):
			flag=1
			break
		x+=1
		level+=1
		value+=1
		#print(values)
	dir[0],dir[1]=dir[1]*-1,dir[0]*1
	if(flag==1):
		break
print(values[(x,y)])
