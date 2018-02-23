from aoc10 import knot_hash
from collections import Counter
from timeit import timeit
import re
import sys

def main():
	# input='ljoxqyyw'
	# used=0
	# matrix=[]
	# for i in range(128):
	# 	hex_repr=knot_hash(input + '-' + str(i))
	# 	hex_number=int(hex_repr,16)
	# 	matrix.append('{:0128b}'.format(hex_number))
	# 	used+=Counter('{:0128b}'.format(hex_number)) ['1']
	# print(used)
	#return hex_number
	matrix=[]
	for line in open('output14','r'):
		matrix.append(line[:-1])

	for i in range(30):
		sys.stdout.write(str(i%10))
	print('')
	for i in matrix[:10]:
		for j in i[:30]:
			if(j=='1'):
				sys.stdout.write('+')
			else:
				sys.stdout.write('-')
		sys.stdout.write('\n')
	prev_regions=None
	current_regions=None
	regions=[]
	counter=0
	sep_counter=0
	no_overlap=None
	for i in range(128):
		current_regions=list(_.span() for _ in re.finditer('1+',matrix[i]))
		counter+=len(current_regions)
		if prev_regions:
			for block in current_regions:
				for region in prev_regions:
					if block[0] in range(region[0],region[1]) or region[0] in range(block[0],block[1]):
						sep_counter+=1
						counter-=1
						if(i<10):
							print('level',i,'\t',block,'\t',region)
		prev_regions=current_regions
			
	print('counter',counter)
	print('sep_counter',sep_counter)
	

if __name__ == '__main__':
	main()