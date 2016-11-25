
# numbers2text.py
#     A program to convert a sequence of Unicode numbers
#     into a string of text.

def main():
   print("This program converts a sequence of Unicode numbers into")
   print("the string of text that it represents.")

   # Get the message to encode
   inString = raw_input("Please enter the Unicode-encoded message: ")

   # Loop through each substring and build Unicode message
#   message = ""
#   for numStr in inString.split():
#      codeNum = eval(numStr)
#      message = message + chr(codeNum)

   # MORE EFFICIENT APPROACH
   chars = []
   for numStr in inString.split():
      codeNum = eval(numStr)
      chars.append(chr(codeNum))

   message = "".join(chars)

   print("The decoded message is: %s") %message

main()
