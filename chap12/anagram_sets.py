def letters(s):
    """Returns the string with the letters of string 
    s in alphabetical order.
    """
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def make_dict():
	"""Creates a dictionary from a text file and then
	returns sets of anagrams"""
	d = {}
	fin = open ('words.txt')
	for line in fin:
		word = line.strip().lower()
		t = letters(word)
		if t not in d:
			d[t] = [word]
		else:
			d[t].append(word)
	return d

def show_anagrams():
	"""Prints all words with at least one anagram."""
	d = make_dict()
	final = []
	for t in d:
		if len(d[t]) > 1:
			final.append(d[t])
	return final

def sort_anagrams():
	"""Sorts the anagrams by the sets with the most 
	words, and prints 10 lines of anagrams. Modified to only
	print anagrams of 8 letters"""
	t = []
	anagrams = show_anagrams()
	for anagram in anagrams:
		t.append((len(anagram),anagram))
	t.sort(reverse=True)
	res = []
	count = 0
	for length, anagramlist in t:
		res.append(anagramlist)
	for i in range(len(res)-1):
		if len(res[i][0]) == 8:
			print res[i]
			count +=1
			if count == 10:
				return

sort_anagrams()
