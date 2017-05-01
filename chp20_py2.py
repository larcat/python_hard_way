#Imports
from sys import argv

# Sets input_file to file exection argv
script, input_file = argv

# Prints a file, f
def print_all(f):
    print f.read()

#Returns to the beginning of a file, f
def rewind(f):
    f.seek(0)

#Prints an number, given by line_count, and the cur line of a file, f
def print_a_line(line_count, f):
    print line_count, f.readline()

#Opens a connection with input_file
current_file = open(input_file)

#Some text to print
print "First let's print the whole file:\n"

#Invokes print_all on f
print_all(current_file)

#Printing
print "Now let's rewind, kind of like a tape."

#Returns to the beginning of current_file
#by invokeing rewind() on it
rewind(current_file)

#Lol print
print "Let's print three lines:"

#Loops through current_file and invokes print_a_line on the cur line
for i in range(1, 4):
    print_a_line(i, current_file)

# Study drills
    # 1) Ok
    # 2) I'm iterating so, 1-3, range in for doesnt include last.
    # 3) Looks good
    # 4) file.seek(..., 0 ) 0 is an arg to "from_what", in this
        #case the beginning (absolute position.) 1 would be the current pos.
    # 5) += adds the argument and assigns the new val to the given var

         