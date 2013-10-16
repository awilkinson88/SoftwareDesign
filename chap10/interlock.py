
def wordlist():
	"""Reads words from a text file"""
	t = []
	fin = open ('words.txt')
	for line in fin:
		word = line.strip()
		t.append(word)
	return t

def interlock (word1, word2):
	"""Creates a new string by alternating the letters of
	two existing strings word1 and word2"""
	h = word1
	k = word2
	r = min(len(h),len(k))
	new = ''
	if h == r:
		b = k[r:]
	else:
		b = h[r:] 
	for i in range (r):
		new += h[i] + k[i]
	return new + b

#print interlock ('shoe','cold')
from bisect import *

def in_list(t,word):
	"""Searches a list for a word using bisection"""
	i = bisect_left(t,word)
	if i != len(t) and t[i] == word:
		return True
	else:
		return False


def searchlist():
	"""Searches a list for words that interlock"""
	lis = []
	t = wordlist()
	for i in range(len(t)-1):
		word = t[i]
		word1 = t[::2]
		word2 = t[1::2]
		if in_list(t,word1):
			if in_list(t,word2):
				lis.append(word)
				lis.append(word1)
				lis.append(word2)
	return lis

print searchlist()