
#Example for definite loops

#Loop 1
def loop1():
   print "Loop 1"
   for x in range(10):
      x = 3.9 * x * (1 - x)
      print x

def loop2():
   print ""
   print "Loop 2"
   for i in [0, 1, 2, 3]:
      print i

def loop3():
   print ""
   print "Loop 3"
   for odd in [1, 3, 5, 7, 9]:
      print odd * odd

def main():
   loop1()
   loop2()
   loop3()

main()
