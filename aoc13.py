def check_severity(data):
	lines=data.split('\n')[:-1]
	layers={}
	layers.fromkeys([for line in lines])

def main():
	with open('input13','r') as file:
		data=file.read()
		check_severity(data)

if __name__=='__main__':
	main()