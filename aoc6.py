import re
import time
file=open("/home/hazkaz/Downloads/input6")
data=file.read()
values=re.split('\s',data)[:-1]
for index,value in enumerate(values):
	values[index]=int(value)

def main():
	def shake():
		counter=max(values)
		start=values.index(max(values))
		limit=len(values)
		values[start]=0
		for i in range(0,counter):
			start=(start+1)%limit
			values[start]=values[start]+1

	ticker=0
	check=set()
	while True:
		if(tuple(values) in check):
			break
		else:
			check.add(tuple(values))
		shake()
		ticker=ticker+1
	print(ticker)

start_time=time.time()

if __name__ == '__main__':
	main()


print("--- %s seconds ---" % (time.time() - start_time))