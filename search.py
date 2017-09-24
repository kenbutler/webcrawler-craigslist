#!/usr/bin/env python

#File name:  search.py
# This is a scrap file for learning web crawling via Python

import contextlib
import re
import sys
import time
import urllib
from bs4 import BeautifulSoup, NavigableString

import csv
from decimal import *

newline = "\n"
invalid_tags = ['b', 'i', 'u', 'span', 'sup', 'em']
wd = "/Users/kenbutler/Desktop/coding/python/output_files/"
date = time.strftime("%B_%d_%Y")
search_location = "search/"

####################################################################

# Library description
#   myLib[state][0][0,1] = info[0,1]
#       info:   0 = state site
#               1 = city count
#
#   myLib[state][1][i][0,1] = city collection
#       city collection     i = unique row of city name & city site
#                           0 = city name
#                           1 = city site
#

####################################################################

def strip_tags(html, invalid_tags):
   soup = BeautifulSoup(html, 'html.parser')

   for tag in soup.findAll(True):
      if tag.name in invalid_tags:
         s = ""

         for c in tag.contents:
            if not isinstance(c, NavigableString):
               c = strip_tags(unicode(c), invalid_tags)
            s += unicode(c)

         tag.replaceWith(s)

   return soup

####################################################################

def exploreCities(myLib, state, search_term):
    str_tmp = ""
    
    try:
        for i in range(0, len(myLib[state][1])):
            term_ct = 0
            url_base = "https:" + myLib[state][1][i][1]
            url = url_base + search_location
            response = urllib.urlopen(url)
            page = response.read()
            # DO NOT PERFORM AN IGNORE TAGS METHOD HERE
            soup = BeautifulSoup(page, 'html.parser')

            print('Searching ' + url)

            # Find all hyperlinks within this city's page
            for link in soup.findAll('a', {"class" : "hdrlnk"}):
                # Make sure there are contents
                if (len(link.contents) > 0):
                    contents = link.contents[0] #Store contents of specific city page
                    # Search for "search_term" in "contents" of specific hyperlink, ignore case
                    if (re.search(search_term, contents, re.I)):
                        # Search term found.  Add to counter
                        term_ct = term_ct + 1
                        str_tmp1 = url_base[0:len(url_base)-1] + link['href'] + " - " + contents
                        str_tmp = str_tmp + str_tmp1 + newline
                        #print '\t' + str_tmp1
  
            if (term_ct > 0):
                str_tmp = str_tmp + "\t\'" + search_term + "\' found " + str(term_ct) + " times at " + url + newline

            # Let the outer for-loop (looping through city websites) sleep for 10 seconds
            # in order to bypass the robot.txt file (e.g. look more like a human)
            print '\tsleeping....'
            time.sleep(10)

    except:
        print ("Exception in exploreCities(): ", sys.exc_info()[0])
        raise

    # Write to file
    temp_file = open(wd + state + "_" + date + ".txt", 'w')
    temp_file.write(str_tmp)
    temp_file.close()
    return str_tmp

####################################################################

def exploreInterface(myLib, state, search_term):
    str_tmp = ""

    try:

        if (state == "ALL"):
            for state_key in myLib:
                temp = exploreCities(myLib, state_key, search_term)
                print temp
                str_tmp = str_tmp + temp

        else:
            str_tmp = exploreCities(myLib, state, search_term)

    except:
        print ("Exception in exploreInterface(): ", sys.exc_info()[0])
        raise

    return str_tmp
####################################################################

def loadLibrary():
    # Associative array
    myLib = {}
    citylist = []
    try:
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
    except IOError:
        print("loadLibrary() - Error interacting with file!")
    except:
        print("loadLibrary() - Error")

    return myLib

####################################################################

def showKeys(myLib):

    # Show available keys
    
    # Initial values
    SC = 20
    str1 = "\t"
    lastKey = " "*SC
    ct = 0
    
    # Loop through keys and display in 4 columns
    for key in myLib:
        str1 = str1 + " "*(SC-len(lastKey)) + key
        ct = ct + 1
        if (ct > 3):
            print str1
            str1 = "\t"
            lastKey = " "*SC
            ct = 0
        else:
            lastKey = key

    # Print anything that's left
    print str1

####################################################################

def menuOptions():

    print("Menu Options:")
    print("")
    print("   MENU or HELP  -   Show menu options")
    print("   CATALOG       -   Show available states")
    print("   INFO <state>  -   Show info about the given state")
    print("   QUIT          -   Exit program")
    print("")
    print("   SEARCH <state> <search_terms>")
    print("     Enter a state and any number of search terms (linked by an AND logical operator)")
    print("     For all states, enter ALL in the state portion.")
    print("")

####################################################################

def decisionMaker(ui, myLib):
    
    full_input = ui.upper()
    iarr = full_input.split(" ") # Split up input string
    key = iarr[0]

    if (key == "CATALOG"):
        showKeys(myLib)
    elif ((key == "MENU") | (key == "HELP")):
        menuOptions()
    elif (key == "INFO"):
        state = iarr[1]
        # Show available cities of state within library
        try:
            print(state + " - " + myLib[state][0][1] + " cities [" + myLib[state][0][0] + "]")
            for i in range(0, len(myLib[state][1])-1):
                print("\t" +  myLib[state][1][i][0] + " "*(30-len(myLib[state][1][i][0])) + myLib[state][1][i][1])
        except:
            print("Invalid state!")
    elif (key == "SEARCH"):
        if (len(iarr) == 1):
            print("You forgot a state to search for!")
            print("Available keys:")
            showKeys(myLib)
        elif (len(iarr) == 2):
            print("You forgot to enter something to search for...")
        else:
            #print("Yay you're searching for %s in %s") %(', '.join(iarr[2:]), iarr[1])
            state = iarr[1]
            output = exploreInterface(myLib, state, iarr[2])
            print output
    else:
        print("Invalid input!  Enter 'help' for valid inputs.")

####################################################################

def inPageBool(url, term):
    
   response = urllib.urlopen(url)
   page = response.read()
   
   keyword_found = term in page

   return keyword_found

####################################################################

def scheduler(argv):

    global wd
    global search_location

    temp = True

    try:
        myLib = loadLibrary()
        # Print for load check
        if False:
            for key in myLib:
                print(key + " - " + myLib[key][0][1] + " cities [" + myLib[key][0][0] + "]")
                for i in range(0, len(myLib[key][1])-1):
                    print("\t" +  myLib[key][1][i][0] + " "*(30-len(myLib[key][1][i][0])) + myLib[key][1][i][1])
        print("******* Database Loaded - %d Keys *******\n") %(len(myLib))

    except:
        print("Error loading database")

    # Use input argument to set search location on Craigslist and
    # working directory for output files
    search_location = "search/" + argv
    print("Search location set to " + search_location)
    if (argv == 'rea'):
        wd = wd + "housing/"
    elif (argv == 'jjj'):
        wd = wd + 'jobs/'
    elif (argv == 'ggg'):
        wd = wd + 'gigs/'
    else:
        print("Cannot properly set working directory! Re-examine code! (" + argv  + ")")
        
    print("Working directory set to " + wd + newline)
    temp = True

    if (temp):
        menuOptions()
    while temp:
        ui = raw_input(">>> ")
        if (ui.upper() == "QUIT"):
            break
        else:
            decisionMaker(ui, myLib)


    #print ("Started scanning Craigslist for " + search_term[0] + "...")

####################################################################

#scheduler(sys.argv[1:])

