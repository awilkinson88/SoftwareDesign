from bisect import *

def in_list(t,word):
	"""Checks to see if a word is in a list by finding the
	index"""
	i = bisect_left(t,word)
	if i != len(t) and t[i] == word:
		return True
	else:
		return False

def wordlist():
	"""Reads words from a text file"""
	t = []
	fin = open ('words.txt')
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

#print in_list(t,'car')

def reversepair():
	"""Searches a list of words for palindromes"""
	t = wordlist()
	lis = []
	for i in range(len(t)):
		word = t[i]
		reverse = word[::-1]
		if in_list(t,reverse):
			lis.append(word)
			lis.append(reverse)
	return lis

print reversepair()