
import csv
from decimal import *

def loadLibrary():
    # Associative array
    myLib = {}
    citylist = []
    with open("library_states_cities.txt", 'rb') as csvfile:
        content = csv.reader(csvfile, delimiter=';')
        for row in content:
            if (len(row) == 4):
                # State
                #print("%s - %d cities available") %(row[1], Decimal(row[3]))
                state = row[1]
                info = [row[2], row[3]]
            elif (len(row) == 3):
                # City
                #print("\t%s") %(row[1])
                citylist.append([row[1], row[2]])
            else:
                # Mesh it together
                if (len(state) > 0):
                    myLib[state] = [info, citylist]
                # Reset values
                citylist = []
                state = ""

        for key in myLib:
            print myLib[key][0]
            for i in range(0, len(myLib[key][1])-1):
                print("\t" +  myLib[key][1][i][0] + "\t" + myLib[key][1][i][1])

loadLibrary()
