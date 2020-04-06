import unittest
import re
import time
file=open("/home/hazkaz/venv/aoc/input9")
data=str(file.read())

def find_garbage_count(data):
	state="none"
	temp_state="none"
	score=0
	level=0
	count=0
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
		
		if(state=='garbage') and temp_state=='garbage':
			count+=1
	# print('score',score,'count',count)
	return count

# <>, 0 characters.
# <random characters>, 17 characters.
# <<<<>, 3 characters.
# <{!>}>, 2 characters.
# <!!>, 0 characters.
# <!!!>>, 0 characters.
# <{o"i!a,<{i<a>, 10 characters
class Unit_Testing(unittest.TestCase):

	def test_cases(self):
		self.assertEqual(find_garbage_count('<>'),0)
		self.assertEqual(find_garbage_count('<<<<>'),3)
		self.assertEqual(find_garbage_count('<{!>}>'),2)
		self.assertEqual(find_garbage_count('<!!>'),0)
		self.assertEqual(find_garbage_count('<random characters>'),17)
		self.assertEqual(find_garbage_count('<!!!>>'),0)
		self.assertEqual(find_garbage_count('<{o"i!a,<{i<a>'),10)

unittest.main()