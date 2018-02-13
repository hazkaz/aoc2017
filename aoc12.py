
def find_connected(data):
	dependency={}
	lines=data.split('\n')[:-1]
	for line in lines:
		dependency_string=line.split('<->')
		dependency[int(dependency_string[0])]=tuple(int(dependant) for dependant in dependency_string[1].split(','))
	connected=set([0])
	flag=1
	while(flag==1):
		flag=0
		for person in dependency:
			combined_set=set([person,*dependency[person]])
			if not connected.isdisjoint(combined_set):
				if not connected.issuperset(combined_set):
					flag=1
				connected.update(combined_set)
	print(len(connected))

def find_groups(data):
	dependency={}
	lines=data.split('\n')[:-1]
	for line in lines:
		dependency_string=line.split('<->')
		dependency[int(dependency_string[0])]=tuple(int(dependant) for dependant in dependency_string[1].split(','))
	groups=[]
	alter_groups=[]
	
	for person in dependency:
		combined_set=set([person,*dependency[person]])
		if(len(groups)==0):
			groups.append(combined_set)
		to_be_joined=[]
		for index,group in enumerate(groups):
			if not group.isdisjoint(combined_set):
				to_be_joined.append(group)
		for item in to_be_joined:
			combined_set.update(item)
			groups.remove(item)
		groups.append(combined_set)

	for group in groups:
		if 0 in group:
			print(len(group))
	print(len(groups))

def main():
	with open('input12','r') as file:
		data=file.read()
		find_groups(data)

if __name__ == '__main__':
	main()