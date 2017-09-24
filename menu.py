#!/usr/bin/env python

#File name:  menu.py
# This is the menu portion for all Craigslist stuff

import search

def showMenu(menuOptions):
    i = 1
    SC = 20
    str1 = "\t"
    lastKey = " "*SC
    dash = "-"

    for option in menuOptions:
        # Sort out label of option
        if (i < 10):
            labelStr = " " + str(i) + dash
        else:
            labelStr = str(i) + dash
        
        # Combine into string
        str1 = str1 + " "*(SC-len(lastKey) - len(labelStr)) + labelStr + option

        # Only break lines after the third options
        if ((i % 3) == 0):
            print str1
            lastKey = " "*SC
            str1 = "\t"
        else:
            lastKey = option
        i += 1
    
    # Print out remainder of string, if there is any
    if ((i % 2) > 0):
        print str1

def main():
    
    optionList = ['Housing', 'Jobs', 'Gigs'];

    # Prompt user for input
    print ("What section of Craigslist would you like to search?")
    showMenu(optionList)

    while True:
        # User input
        ui = raw_input("Choice >> ")

        if (ui.lower() == 'quit') or (ui.lower() == 'exit'):
            break
        
        # Read user input.  Make sure it's a number
        try:
            choice = int(ui)
        except:
            print("Input must be a number!")
            continue

        # Use user input to send key to search script
        temp_arr = ['rea', 'jjj', 'ggg']
        if (choice < len(temp_arr) + 1):
            key = temp_arr[choice-1]
            search.scheduler(key)
            break
        else:
            print("Selection out of range!")

    print "Closing program"

main()
