import re
import time
file=open("input6")
data=file.read()
values=[int(item) for item in re.split('\s',data)[:-1]]

def main():
	def shake():
		counter=max(values)
		start=values.index(max(values))
		limit=len(values)
		values[start]=0
		for i in range(0,counter):
			start=(start+1)%limit
			values[start]=values[start]+1

	def one():
		ticker=0
		check=set()
		while True:
			if(tuple(values) in check):
				if('count' in locals()):
					print(count)
				count=0
				check.remove(tuple(values))
			else:
				check.add(tuple(values))
				ticker+=1
				if('count' in locals()):
					count+=1
			shake()
		print(ticker)

	def two():
		ticker={}
		check=set()
		while True:
			if(tuple(values) in check):
				ticker[tuple(values)]=0
				print(tuple(values))
				#print(ticker[tuple(values)])
				ticker[tuple(values)]=0
			else:
				check.add(tuple(values))
				ticker[tuple(values)]=0
			shake()
			
		print(ticker)

	one()
start_time=time.time()

if __name__ == '__main__':
	main()


print("--- %s seconds ---" % (time.time() - start_time))