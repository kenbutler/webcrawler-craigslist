
# username.py
#   Simple string processing program to generate username.

def main():
   print "This program generates a computer username.\n"

   # Get user's first and last name
   first = raw_input("Please enter your first name:\n")
   first = first.lower()
   last = raw_input ("Please enter your last name:\n")
   last = last.lower()

   # Concatenate first initial with first 7 letters of last name
   uname = first[0] + last[:7]

   print "Your username is: %s\n" %uname

main()
