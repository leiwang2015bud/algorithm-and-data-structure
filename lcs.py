class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        c = [[0 for j in range(n+1)]  for i in range(m+1)]
        b = [[0 for j in range(n+1)]  for i in range(m+1)]
        for i in range(1,m+1):
          for j in range(1,n+1):
            if A[i-1]==B[j-1]:
              c[i][j]= c[i-1][j-1]+1
              b[i][j]=1
            elif c[i-1][j]>=c[i][j-1]:
              c[i][j]=c[i-1][j]
              b[i][j]=2
            else:
              c[i][j]=c[i][j-1]
              b[i][j]=3
        l = max(max(c))
        self.printSolution(A,b,m,n)
        return (l,b)

    def printSolution(self,A,b,i,j):
        if i==0 or j==0:
          return "Print End!"
        if b[i][j]==1:
          print A[i-1]
          return self.printSolution(A,b,i-1,j-1)
        elif b[i][j]==2:
          return self.printSolution(A,b,i-1,j)
        else:
          return self.printSolution(A,b,i,j-1)


print Solution().longestCommonSubsequence("ABCD","EACB")
