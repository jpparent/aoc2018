import re

f = open('03-1.input')
rows = f.readlines()
f.close()

fabric = [[0 for x in range(0,1000)] for y in range(0,1000)]

clashes = 0
intactClaims = {} # {key:id, value:isClaimIntact}

for row in rows:
	result = re.search('#(.*) @ (.*),(.*): (.*)x(.*)', row)
	id = result.group(1)
	x = int(result.group(2))
	y = int(result.group(3))
	w = int(result.group(4))
	h = int(result.group(5))

	for i in range(0,w):
		for j in range(0,h):
			if fabric[x+i][y+j] == 0:
				fabric[x+i][y+j] = id
				if id not in intactClaims or intactClaims[id] is not False:
					intactClaims[id] = True
			elif fabric[x+i][y+j] != 'X':
				intactClaims[fabric[x+i][y+j]] = False
				intactClaims[id] = False
				fabric[x+i][y+j] = 'X'
				clashes += 1

print(clashes)
for id, intact in intactClaims.items():
    if intact:
        print(id)
        break