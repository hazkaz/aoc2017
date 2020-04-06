import re
import time
from collections import Counter
file=open("input7")
data=file.read()
lines=data.split('\n')[:-1]
dictionary={}
def main():
	def odd_one_out():
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

	def odd_weight_out():
		for line in lines:
			datum=line.split()
			if(len(datum)>2):
				sub=[_.strip(',') for _ in datum[3:]]
				print("sub",sub)
				weights=[]
				for child in sub:
					for _line in lines:
						if _line.startswith(child):
							weights.append(int(_line.split()[1][1:-1]))
							print("line",_line,"weights",weights)
	
	def dict_from_lines(lines):
		dictionary={}

	def find_weight(lines,query):
		for line in lines:
			if(line.startswith(query)):
				return int(line.split()[1][1:-1])

	def bfs(lines,root='rqwgj',weights={}):
		for line in lines:
			if(line.startswith(root)):
				#if it has children
				if(len(line.split())>3):
					children=[child.strip(',') for child in line.split()[3:]]
					total=[]
					for child in children:
						total.append(bfs(lines,child))
					counter=Counter(total)
					# print(counter)
					if(counter[min(counter,key=counter.get)]==1):
						print("odd", "root", root, "children", children, "weights of children", total)

				#leaf node
				else:
					return int(line.split()[1][1:-1])
				return(sum(total)+int(line.split()[1][1:-1]))
	print(bfs(lines))
if __name__ == '__main__':
	main()