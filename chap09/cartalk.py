def readmoby():

	fin = open ('words.txt')
	for line in fin:
		word = line.strip()
		if has3letters(word):
			print word


def has3letters (str):
	count = 0
	i = 0
	while i < len(str)-1:
		if str[i+1] == str[i]:
			count = count+1
			i = i+2
			if count == 3:
				return True
		else:
			count = 0
			i = i+1
		

	else:
		return False
	
#readmoby()

def is_palindrome2 (word):
	if word == word[::-1]:
		return True
	else:
		return False

def puzzler2(string):
	if is_palindrome2(string[2:6]):
		num = str(int(string)+1)
		if is_palindrome2(num[1:6]):
			num2 = str(int(num)+1)
			if is_palindrome2(num2[1:5]):
				num3 = str(int(num2)+1)
				if is_palindrome2(num3):
					return True
	return False

def check_nums():

#Referenced solution in book in order to figure out how
#to test numbers

	i = 100000
	while i <= 999999:
		input = str(i)
		if puzzler2(input):
			print input
		i = i+1

check_nums()
