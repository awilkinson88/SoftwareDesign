
def read_dict():
	"""Creates a dictionary from a text file with
	words as keys"""
	d = {}
	fin = open ('words.txt')
	for line in fin:
		word = line.strip()
		d[word] = word
	return d

def find_children(s,d):
	"""Returns a list of new words that be created by 
	deleting a letter from a word"""
	res = []
	t = list(s)
	for i in range(len(s)):
		newstr = t[:]
		del newstr[i]
		delimiter = ''
		ts = delimiter.join(newstr)
		if ts in d:
			res.append(ts)
	return res

memo = {}
memo[''] = ['']

def is_reducible(s,d):
	"""Returns all the new English words that can be created
	from a parent word by deleting one letter at a time."""
	if s in memo:
		return memo[s]
	kids = find_children(s,d)
	if kids == []:
		return [s]
	for child in kids:
		t = is_reducible(child,d)
		if t:
			kids += t
		memo[s] = kids
		return kids


def find_reducible(d):
	"""Returns all the words that are reducible and have
	at least one new word that can be created by removing
	a letter"""
	res = []
	for line in d:
		thing = is_reducible(line,d)
		if thing[-1] == '':
			res.append(line)
	return res

def find_longest(d):
	"""Returns the longest word that is completely
	reducible to the empty string."""
	words = find_reducible(d)
	t =[]
	for word in words:
		t.append((len(word),word))

	t.sort(reverse=True)
	res = []
	for length,word in t:
		res.append(word)
	return res[0]

#d = read_dict()
#print find_reducible(d)
#print find_longest(d)
#print is_reducible('complecting',d)