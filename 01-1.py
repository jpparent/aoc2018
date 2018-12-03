f = open('01-1.input')
rows = f.readlines()
f.close()

frequency = 0

for change in rows:
	frequency += eval(change)

print(frequency)