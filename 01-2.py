f = open('01-1.input')
rows = f.readlines()
f.close()

def find():
	frequency = 0
	history = []
	history.append(frequency)

	while 1==1:
		for change in rows:
			frequency += eval(change)
			if frequency not in history:
				history.append(frequency)
			else:
				return frequency

print(find())