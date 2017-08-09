# worst cases: O(n^2)
# best cases: O(n)
def INSERTIONSORT_in(A): 
  for j in range(1,len(A)):
    key=A[j]
    i = j-1
    while( i>=0 and key<A[i]):
      A[i+1]=A[i]
      i = i -1
    A[i+1]=key # when key>A[i]
  return A

def INSERTIONSORT_de(A): 
  for j in range(1,len(A)):
    key=A[j]
    i = j-1
    while( i>=0 and key>A[i]):
      A[i+1]=A[i]
      i = i -1
    A[i+1]=key # when key>A[i]
  return A

print INSERTIONSORT_de([4,5,2,1,0])