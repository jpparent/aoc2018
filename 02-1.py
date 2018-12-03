from collections import Counter

f = open('02-1.input')
rows = f.readlines()
f.close()

twices = 0
thrices = 0

for id in rows:
	counter = Counter(id)
	foundTwice = False
	foundThrice = False
	for char,count in counter.items():

		if count == 2 and not foundTwice:
			twices += 1
			foundTwice = True
			
		elif count == 3 and not foundThrice:
			thrices +=1
			foundThrice = True

print(twices * thrices)