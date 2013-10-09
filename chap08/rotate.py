##Author: Anne Wilkinson - Referenced solution code
##by Allen Downey when stuck, didn't account for start
#condition

def rotate_letter(letter,int):

	number = ord(letter) - ord('a')
	rotated = chr ((number + int) %26 + ord('a'))
	return rotated

def rotate_word (str, int):
	res = ''
	for letter in str:
		res += rotate_letter(letter, int)
    	return res
	

print rotate_letter('r',13)
print rotate_word('car',13)
