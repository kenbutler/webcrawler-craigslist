
# Computes factorial

def main():
   print "   This program computes the factorial of a given integer."
   n = input("Please input an integer: ")

   fact = 1
   for factor in range(n, 1, -1):
      fact = fact * factor

   print "The factorial is %d" %fact

main()
