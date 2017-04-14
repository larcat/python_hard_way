#Imports the argv function from sys lib
from sys import argv

#Specifies that filename is going to come from the argv at command line
script, filename = argv

#Saves the readin file as var named 'txt'
txt = open(filename)

#Prints the filename, saved conveniently as var 'filename'
print "Here's your file %r:" % filename
#Prints the result of the readin
print txt.read()

#Prints input prompt
print "Type the filename again:"
#Saves the retyped filename after input from '>' prompt
file_again = raw_input(">")

#Reads in the new filename from above
txt_again = open(file_again)

#Prints out the new filename from prompt
print txt_again.read()

txt.close()
txt_again.close()

#Study drills
    #1 Ok
    #2 Yup
    #3 Word
    #4 Print's out the file contents the one time....
    #5 Errors out because it expected an argument
    #6 print of the open() is...
        #<open file 'ex15_sample.txt', mode 'r' at 0x0000000001E721E0>
        #print varname.read() gives expected
    #7 Have to do varname.close()
        #Opposite order from R
