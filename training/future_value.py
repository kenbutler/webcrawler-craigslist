
# Program that calculates the future value of an investment

def main():
   print "   This program calculates the future value"
   print "   of an investment after a certain number of years."

   principal = input("Enter the initial principal value: ")
   apr = input("Input the annual interest rate (%): ")
   apr = apr / 100.0 #Turn percentage input to decimal value
   years = input("Input the number of years invested: ")

   for i in range(years):
      principal = principal * (1 + apr)

   print "Final investment value of $%.2f" %principal

main()
