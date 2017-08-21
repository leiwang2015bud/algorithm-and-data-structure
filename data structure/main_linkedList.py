from classes.linklist import LinkedList

link = LinkedList(5)
link.add(900,100,"lily")
link.add(100,80,"lixia")

print link._count
l = link.getResult()
for i in range(0,link._count):
  print l.next.value