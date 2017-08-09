# Start with the entire sequence of elements.
# wrost case: O(log(n))
# best case: omega(1)
def binarySearch( nums, target):
	low = 0
	high = len(nums)-1
	# Repeatedly subdivide the sequence inhalf until the target if found.
	while low < high:
		# Find the midpoint of the sequence 
		mid = high+low//2 # in python 3.x, 4/3=1.3333 4//3=1
		# Does the midpoint contain the target?
		if nums[mid] == target:
			return True
		# Or does the target precede the midpoint?
		elif target < nums[mid]:
			high = mid -1
		else:
			low = mid + 1

	# If the sequence cannot be subdivided further, we're done
	return False

print binarySearch([2,4,6,8,9],4)

def binarySearch_simple( nums, target):
	low = 0
	high = len(nums)-1
	while low < high:
		mid = high+low/2
		if nums[mid] == target:
			return True
		elif target < nums[mid]:
			high = mid -1
		else:
			low = mid + 1
	return False