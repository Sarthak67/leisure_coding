import collections
class Solution:
	def commonality(self,s):
		out=0
		c1=collections.Counter(' ')
		c2=collections.Counter(s)
		for i,c in enumerate(s):
			c1[c]+=1
			c2[c]-=1
			out=max(out,sum((c1&c2).values()))


		return out


s = Solution()
print(s.commonality('abcdedeara'))



