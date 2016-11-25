
# Computes the quadratic function given A, B, C

import math # Makes the math library available

def main():
   print "This program finds the real solution to a quadratic equation."

   a, b, c = input("Please enter the coefficients (a, b, c): ")
   if (b**2 >= 4*a*c):
      discRoot = math.sqrt(b*b - 4*a*c)
      root1 = (-b + discRoot) / (2*a)
      root2 = (-b - discRoot) / (2*a)
      print "The roots are %.4f, %.4f" %(root1, root2)
   else:
      print "Imaginary values exist here.  Cannot compute."

   

main()
