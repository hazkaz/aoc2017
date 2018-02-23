import numpy as np
import math
import sys
file=open("/home/hazkaz/venv/aoc/input11")
data=file.read()
values=data.split()[0].split(',')

eqv={'n':np.array([0,1]),
's':np.array([0,-1]),
'ne':np.array([math.cos(30*math.pi/180),math.sin(30*math.pi/180)]),
'se':np.array([math.cos(-30*math.pi/180),math.sin(-30*math.pi/180)]),
'sw':np.array([-math.cos(30*math.pi/180),-math.sin(30*math.pi/180)]),
'nw':np.array([-math.cos(-30*math.pi/180),-math.sin(-30*math.pi/180)])
}

def converter(array):
	return array[0]*eqv.get('n')+array[1]*eqv.get('ne')+array[2]*eqv.get('se')

dir=dict({'n':np.array([1,0,0]),
	's':np.array([-1,0,0]),
	'nw':np.array([0,0,-1]),
	'sw':np.array([0,-1,0]),
	'ne':np.array([0,1,0]),
	'se':np.array([0,0,1])})

start=np.array([0,0,0])

def distance_finder(start):
	current=np.array([0,0,0])
	steps=0
	while(not np.array_equal(current,start) and steps<10):
		mags={}
		min=-1

		distance=np.linalg.norm(converter(start)-converter(current))
		if(distance==0):
			break;
		for choice in dir:
			if(min==-1):
				min=choice
				print(choice,np.linalg.norm(converter(start)+converter(dir.get(min))-converter(current)))
			else:
				min=choice if distance<=np.linalg.norm(converter(start)+converter(dir.get(min))-converter(current)) else min
				print(choice,np.linalg.norm(converter(start)+converter(dir.get(min))-converter(current)))
		current-=dir.get(min)
		steps+=1
		print(current,start)
	print("The number of steps",steps)

for directions in values[:5]:
	start+=dir.get(directions)
	
print(start)
distance_finder(start)