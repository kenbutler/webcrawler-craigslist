
# dateconvert.py
#  Converts a date in form "mm/dd/yyy" to "month day, year"

def main():
   # Get the date
   dateStr = raw_input("Enter a date (mm/dd/yyyy): ")

   # Split the date in 3
   monthStr, dayStr, yearStr = dateStr.split("/")

   # Convert strings to integers
   month = int(monthStr)
   day = int(dayStr)
   year = int(yearStr)

   months = (["January", "February", "March", "April",
              "May", "June", "July", "August", "September",
              "October", "November", "December"])

   print("%s %d, %d") %(months[month-1], day, year)

main()
