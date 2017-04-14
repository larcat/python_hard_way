from sys import argv
#from os.path import exists

script, from_file, to_file = argv

#print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on one line, how?
# Here's how

open(to_file, 'w').write(open(from_file).read())
    # PYTHON JUST MAKES SENSE U C?!?!?!?

#print "The input file is %d bytes long" % len(indata)

#print "Does the output file exist? %r" % exists(to_file)
#print "Ready, hit RETURN to continue, CTRL-C to abort."
#raw_input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

#print "Alright, all done."
#print "Copied %s to %s" % (from_file, to_file)

#out_file.close()
#in_file.close() -- Str now, not a connection