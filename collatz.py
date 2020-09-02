import math
import collections


def collatz():
	master=[]
	for i in range(4,50,2):
		master.append((2**i-1)/3)

	print(master)

	assoc=[]
	for i in range(1,1000000,1):
		x=i
		a=i
		while x != 1:
			if x % 2 > 0:
				x =((3 * x) + 1)
			else:
				x = (x / 2)
				if x in master:
					#print(a,341)
					assoc.append(x)
					break
				else:
					continue


	return assoc


a=collatz()
aa=dict(collections.Counter(a))
print(aa)
#print(100000-aa[5]+aa[85]+aa[21]+aa[341])

