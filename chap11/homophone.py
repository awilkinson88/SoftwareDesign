##Author: Anne Wilkinson

def make_dict():
	"""Creates a dictionary from a text file"""
	d = {}
	fin = open ('words.txt')
	for line in fin:
		word = line.strip()
		d[word] = word
	return d

def is_homophone(word1,word2):
	"""Checks if two words are pronounced the same"""
	pdi = read_dictionary()
	if word1 not in pdi or word2 not in pdi:
		return False
	return pdi[word1] == pdi[word2]


def puzzler4(word,di):
	"""Checks if a word sounds the same when the 
	first and second letter are removed."""
	phone1 = word[1:]
	phone2 = word[0] + word[2:]
	if len(word) != 5:
		return False
	if phone1 not in di:
		return False
	if phone2 not in di:
		return False
	if not is_homophone(word,phone1):
		return False
	if not is_homophone(phone1,phone2):
		return False
	return True
				
def find_word(di):
	"""Searches a dictionary for a word that fits the 
	properties of Puzzler 4"""
	res = []
	for line in di:
		if puzzler4(line,di):
			res.append(line)
	return res

di = make_dict()
from pronounce import read_dictionary
print find_word(di)
#print is_homophone('there','their')
#answer is llama and scent