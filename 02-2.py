from collections import Counter

f = open('02-1.input')
rows = f.readlines()
f.close()

for i in range(0, len(rows)-1):
	for j in range(i+1, len(rows)):
		a = rows[i]
		b = rows[j]
		same = [a[ii] for ii in range(len(b)) if a[ii] == b[ii]]
		if len(same) == len(rows[i]) - 1:
			print(''.join(same))
