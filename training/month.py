
# month.py
#  This program prints the abbreviation of a month, given its number

def main():
   print "This program prints the abbreviation of a month given its number.\n"
   monthAbbrs = "JanFebMarAprMayJunJulAugSepOctNovDec"
   monthNames = ["January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]   
   pos = 1
   while True:
      n = input("What is the number of the month? ")
      pos = (n-1)*3
      if ((n > 0) & (n < 13)):
         break
      else:
         print "Not a valid month! (1-12)  Try again.\n"
   print "The abbreviation for the %d month is %s (%s)\n" %(n, monthAbbrs[pos:pos+3], monthNames[n-1])


main()
