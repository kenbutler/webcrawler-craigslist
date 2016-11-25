

# text2numbers.py
#    A program to conver a textual message into a sequence of
#       numbers, utilizing the underlying Unicode encoding.

def main():
   print "This program converts a textual message into a sequence"
   print "of numbers representing the Unicode encoding of the message."

   # Get the message to encode
   message = raw_input("Please enter the message to encode: ")

   print ("Here are the Unicode codes:")

   #Loop through the message and print out the Unicode values
   for ch in message:
      print("%d") %ord(ch)

main()
