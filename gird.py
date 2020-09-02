class Solution:
	def find(self,Input,rule,turn):
		M1=Input
		rule=[1 if rule[i]=='alive' else 0 for i in range(len(rule))]
		for i in range(turn):
			M1=self.Calculate_live(Input)
			M2=self.Calculate_new(M1,rule)

			Input=M2
		return Input


	def Calculate_live(self,Input):
		N=[[0,0,0,0],[0,0,0,0]]
		N[0][0]=Input[0][1]+Input[1][0]+Input[1][1]
		N[0][1]=Input[0][0]+Input[1][1]+Input[1][0]+Input[0][2]+Input[1][2]
		N[0][2]=Input[0][3]+Input[0][1]+Input[1][1]+Input[1][2]+Input[1][3]
		N[0][3]=Input[0][2]+Input[1][2]+Input[1][3]
		N[1][0]=Input[0][0]+Input[0][1]+Input[1][1]
		N[1][1]=Input[0][0]+Input[0][1]+Input[1][0]+Input[0][2]+Input[1][2]
		N[1][2]=Input[0][3]+Input[0][1]+Input[1][1]+Input[0][2]+Input[1][3]
		N[1][3]=Input[0][2]+Input[1][2]+Input[0][3]
		return N

	def Calculate_new(self,M1,rule):
		#print(M1)
		for i in range(2):
			for j in range(4):
				#print(i,j)
				M1[i][j]=rule[M1[i][j]]
		return M1



s= Solution()
print(s.find([[0, 1, 1, 0], [1, 1, 0, 0]],["dead", "dead", "dead", "alive", "dead", "alive", "dead", "dead", "dead"],2))


