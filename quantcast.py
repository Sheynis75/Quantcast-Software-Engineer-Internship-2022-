import sys

def Most_Active_Cookie():
    print(sys.argv[0])                                                      # command line for python

cookie_file = open(sys.argv[0], "r")                                        # opens the file containing the cookies
date_given = str(sys.argv[3])                                               # takes the given date and stores it as a string
cookies = {}                                                                # stores each cookie and keep track of how many times it occurs.

for line in cookie_file.readlines():                                        # start by looping over each line in the file
    cookie, cookie_date = line.split(",")                                   # splits the data in each line by the comma between cookie and time
    cookie_date = cookie_date[0:10]                                         # indexes the string to only contain the dates
    if (date_given == cookie_date):                                         # checks to see whether the date given matches the date associated with the cookie currently being looked at in the loop 
        if cookie in cookies:                                               # checks to see whether or not cookie is in dictionary, if it is, increment by 1
            cookies[cookie] += 1
        else:                                                               # if cookie is not present, add it to dictionary with value 1
            cookies[cookie] = 1

all_occurrences = cookies                                                   # get all the values within the dictionary
max_occurences = max(all_occurrences)                                       # finds the max value in the dictionary

for key in cookies:                                                         # loop through the dictionary 
    if cookies[key] == max_occurences:                                      # check to see which cookies occurred the most 
        print(key) 

cookie_file.close()                                                         # once all the functions are ran, we must close the file