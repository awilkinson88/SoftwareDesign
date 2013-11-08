class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second"""
	#We can create a new Time object
	#and assign attributes for hours, minutes, and seconds:
time = Time()
time.hour = 11
time.minute = 59
time.second = 30

#from datetime import *

current = Time()
current.year = 2013
current.month = 11
current.day = 3
current.hour = 15
current.minutes = 23
current.seconds = 9

birthday = Time()
birthday.year = 1994
birthday.month = 5
birthday.day = 25
birthday.hour = 0
birthday.minutes = 0
birthday.seconds = 0

def time_to_bday(current,birthday):
	age = current.year-birthday.year
	print age
	print 12-current.month+birthday.month
	print birthday.day-current.day
	print 

time_to_bday(current,birthday)




# # def print_time(time_obj):
# 	print time.hour
# 	print time.minute
# 	print time.second

# print_time(time)
# print time

# def is_after(time1,time2):
	# return (time1.hour,time1.minute,time1.second) < (time2.hour,time2.minute,time2.second)

# print is_after(time,time2)