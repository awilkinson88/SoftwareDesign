#Author: Anne Wilkinson

def rotate_letter(letter,int):
	"""Rotates a letter by int characters"""
	number = ord(letter) - ord('a')
	rotated = chr ((number + int) %26 + ord('a'))
	return rotated

def rotate_word (str, int):
	"""Rotates a word by int characters"""
	res = ''
	for letter in str:
		res += rotate_letter(letter, int)
    	return res

def make_dict():
	"""Creates a dictionary from a text file"""
	d = {}
	fin = open ('words.txt')
	for line in fin:
		word = line.strip()
		d[word] = word
	return d

def rotated_pairs(di):
	"""Searches a dictionary for words that are a 
	rotated pair, and prints by how much they are
	rotated."""
	t = []
	for word in di:
		for i in range (1,25):
			rotated = rotate_word(word,i)
			if rotated in di:
				t.append(word)
				t.append(rotated)
				t.append(i)
	return t

di = make_dict()
print rotated_pairs(di)
