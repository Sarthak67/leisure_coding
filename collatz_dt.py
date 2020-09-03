import timeit
class collatz:
	table={}
	primary_key={}
	columns={}
	values={}
	def __init__(self, tableName,primaryKey,columns):
		self.table[tableName]=self.assign_table()
		key=self.assign_primaryKey(tableName)
		self.primary_key[key]=[0,0]
		for i in range(len(columns)):
			if columns[i]!=primaryKey:
				self.columns[columns[i]]=(4**i)*key
				self.primary_key[key][1]+=1



	def assign_table(self):
		values=list(self.table.values())
		if len(values)==0:
			return 5
		else:
			return values[-1]*4+1 if (values[-1]*4+1)%3!=0 else 16*values[-1]+5

	def assign_primaryKey(self,tableName):
		return self.table[tableName]*4 if self.table[tableName]%3==1 else self.table[tableName]*2




def input(collatz,tablename,values):
	if tablename not in list(collatz.table.keys()):
		return'Please input valid table name'
	else:
		numberOfValues=len(values)
		tableIndex=collatz.table[tablename]
		data_keys=collatz.values.keys()
		primaryKeyIndex=tableIndex*2**(((tableIndex%3)%2)+1)
		for i in range(numberOfValues):
			collatz.values[int(((primaryKeyIndex*4**(i))-1)/3)*4**collatz.primary_key[primaryKeyIndex][0]]=values[i]


		collatz.primary_key[primaryKeyIndex][0]+=1

		


def search(collatz,tablename,value):
	return_keys=[]
	return_value=[]
	if tablename not in list(collatz.table.keys()):
		return'Please input valid table name'
	tableIndex=collatz.table[tablename]
	primaryKeyIndex=tableIndex*2**(((tableIndex%3)%2)+1)	
	column_names,search_value=value.split('=')
	if  column_names not in list(collatz.columns.keys()):
		return 'Please input valid column name'
	column_index=collatz.columns[column_names]
	index=collatz.primary_key[primaryKeyIndex][0]
	for i in range(index):
		if(collatz.values[int((column_index-1)/3)*4**i]==search_value):
			return_keys.append(i)

	for j in return_keys:
		return_value1=[]
		for i in range(collatz.primary_key[primaryKeyIndex][1]):
			return_value1.append(collatz.values[int(((primaryKeyIndex*4**(i))-1)/3)*4**j])
		return_value.append(return_value1)

	return return_value


	




def create(query):
	table_name=query.split('create table')[1].split('(')[0].strip()
	primary_key=query.split('primary key')[1].strip()
	columns=query.split('(')[1].split(')')[0].split(',')	
	a=collatz(table_name,primary_key,columns)
	print(a.table)
	print(a.primary_key)
	print(a.columns)
	for i in range(10000):
		input(a,'table_name',[str(i),str(i),'1',str(i),'1',str(i)])
	start = timeit.default_timer()
	print(search(a,'table_name','x=1'))
	stop = timeit.default_timer()
	print('Time: ', stop - start)  






create('create table table_name(x,y,z,a,b,c)primary key 0')
