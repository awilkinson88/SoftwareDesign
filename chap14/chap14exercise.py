#Answer to exercise 12.14

import urllib


# conn = urllib.urlopen('http://thinkpython.com/secret.html')
# for line in conn:
# 	print line.strip()


zipcode = raw_input('Enter the zipcode')
url = 'http://www.uszip.com/zip/' + zipcode
zipsearch = urllib.urlopen(url)
for line in zipsearch:
	line = line.strip()
	if 'Population' in line:
		print line
	if 'Longitude' in line:
		print line
	if 'Latitude' in line:
		print line

zipsearch.close()
