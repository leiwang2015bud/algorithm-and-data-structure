from classes.binarysearchtree import BSTMap

K = [80,99,100,70,60]
V = ["bob","alice","lily","tom","LiXia"]
bst = BSTMap()
for i in range(0,len(K)):
  bst.add(K[i],V[i])

it = bst.__iter__()
print "Beauty score: "
try:
  while True:
    print it.__next__()
except StopIteration:
  pass

score = 100
print "\nWho get the score of ",score
print "hi,it's",bst.valueOf(score)

print "\nWho is the top 1 beauty ?"
print bst.valueOfMax()

print "\nWho is the tail of beauty ?"
print bst.valueOfMin()

bst.remove(score)
it = bst.__iter__()
print "Beauty score: "
try:
  while True:
    print it.__next__()
except StopIteration:
  pass

