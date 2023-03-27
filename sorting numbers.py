class Solution:
   def solve(self, n):
      res=[]
      while n%2==0:
         res.append(2)
         n//=2
      for i in range(3,int(n**.5)+1,2):
         while n%i==0:
            res.append(i)
            n//=i
      if n>2:
         res.append(n)
      return res
ob = Solution()
print(ob.solve(42))