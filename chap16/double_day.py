from datetime import *

bday = datetime(1994,05,25)
bday2 = datetime(1990,9,11)

current =  datetime.today()
# print current.weekday()
# print current.strftime('%A')

def time_to_bday(bday,current):
	"""Takes a birthday as an input and prints
	the time remaining until their next one"""
	nextbday = datetime(current.year,bday.month,bday.day)
	if nextbday < current:
		nextbday = nextbday = datetime(current.year+1,bday.month,bday.day,0)
	twait = nextbday - current
	print 'Age:', nextbday.year-bday.year
	print 'Time to Bday:', twait

time_to_bday(bday,current)

def double_day(bday1,bday2):
	"""Takes two birthdays as an input and finds on
	what day one person is twice as old as the other"""
	younger = max(bday1,bday2)
	older = min(bday1,bday2)
	dif = younger-older
	dday =  dif + younger
	print 'Double Day:', dday
	# print dday-older
	# print dday-younger

double_day(bday,bday2)