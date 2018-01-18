import re
import time
file=open("/home/hazkaz/venv/aoc/input9")
data=str(file.read())


state="none"
temp_state="none"
score=0
level=0
for char in data:

	#previous symbol was '!'
	if(state=="skip"):
		state=temp_state
		continue

	temp_state=state

	if(state=='garbage' and char=='!'):
		state='skip'

	if(state!='garbage' and char=='{'):
		state="group"
		level+=1

	if(state!='garbage' and char=='}'):
		score+=level
		level-=1

	if(state!='garbage' and char=='<'):
		state="garbage"

	if(state=='garbage' and char=='>'):
		state='group'
		
print(score)