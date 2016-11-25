

def reverseArray(array, start, end):

   tmp1 = array[start]
   array[start] = array[end]
   array[end] = tmp1
   if (start+1 < end-1):
      reverseArray(array, start + 1, end - 1)

def main():
   
   arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
   print "Original Array:"
   print arr1
   print ""
   reverseArray(arr1, 0, len(arr1) - 1)
   print "Reversed Array:"
   print arr1
   print ""

main()
