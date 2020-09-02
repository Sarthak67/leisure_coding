import collections as col
#ab|cd,ab|cd,ab|de,ac|de,bc|de

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


    def PrintTree(self):
    	print(self.data)
    	if self.left:
    		self.left.PrintTree()
    	if self.right:
    		self.right.PrintTree()


    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
       

    def insert1(self,data):
    	self.left=Node(data[0])
    	self.right=Node(data[1])



    def all_quartet(self,b,l):
    	#print(l)
    	#print(b)
    	if(len(b)==1):
    		#print(list(b[0].split('|')[0]))
    		l.append(list(b[0].split('|')[0]))
    		l.append(list(b[0].split('|')[1]))
    		return(l)
    	else:
    		c=[]
    		for i in b:
    			c=c+(i.split('|'))
    		most_frequent=dict(col.Counter(c))
    		most_frequent_list = list(max(most_frequent, key=most_frequent.get))
    		l.append(most_frequent_list)
    		cc=[]
    		for i in b:
    			flag=True
    			for j in i.split('|'):
    				if most_frequent_list[0] in list(j):
    					flag=False
    					break
    			if flag:
    				cc.append(i)

    		return self.all_quartet(cc,l)


node=Node(10)
node11=Node(None)
a = input()
b=a.split(',')
d=node11.all_quartet(b,[])
node1=[Node(i-int(len(d)/2)) for i in range(len(d))]
for i in range(len(d)):
	#sprint('i',(i-int(len(d)/2)))
	node.insert((i-int(len(d)/2)))

for i in range(len(d)-1,-1,-1):
	node1[i].insert1(d[i])

#print(111+node.data)
node.PrintTree()