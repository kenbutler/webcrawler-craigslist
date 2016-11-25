
# Description here
# Author: Ken Butler


def main():
   print "This program takes an alphabetical letter (input) and presents the"
   print "ASCII ordinal value of it."

   while True:
      letter = raw_input("Please input a letter: ")
      if (len(letter) == 1):
         print "Letter Value: %s" %letter
         print "Ordinal Val : %d" %ord(letter)
         break
      else:
         print "Must be a letter!  Length must be 1."

   print "\n------ ASCII Key ------\n"
   for num in range(64):
      i = num * 4
      if (i < 10):
         print ("%d = %s     %d = %s     %d = %s     %d = %s"
            %(i, chr(i), i+1, chr(i+1), i+2, chr(i+2), i+3, chr(i+3)))
      elif (i < 100):
         print ("%d = %s    %d = %s    %d = %s    %d = %s"
            %(i, chr(i), i+1, chr(i+1), i+2, chr(i+2), i+3, chr(i+3)))
      else:
         print ("%d = %s   %d = %s   %d = %s   %d = %s"
            %(i, chr(i), i+1, chr(i+1), i+2, chr(i+2), i+3, chr(i+3)))

main()
