def searchByHashMap(nums,target):
    d = {i: False for i in nums}
    if d.get(target) is not None:
        return True
    else:
        return False

print searchByHashMap([100,4,200,1,3,2],2)
