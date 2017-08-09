# worst case: O(nlog(n))
# best case: omega()
def merge(L,R):
	n = len(L) + len(R)
	L.append(float('inf'))
	R.append(float('inf'))
	result = [None]*(n)
	i,j = 0,0
	for k in range(0,n):
		if L[i]<=R[j]:
			result[k]=L[i]
			i += 1
		else:
			result[k]=R[j]
			j += 1
	return result

def mergeSort(A):
	if len(A)<2:
		return A
	else:
		q = len(A)/2
		L = mergeSort(A[:q])
		R = mergeSort(A[q:])
		result = merge(L,R)
		return result

print mergeSort([2,1,0,4,3])