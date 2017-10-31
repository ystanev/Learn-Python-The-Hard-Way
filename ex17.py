from sys import argv
# from os.path import exists

script, from_file, to_file = argv

# print "Copying from %s to %s." % (from_file, to_file)

in_file = open(from_file)   # Opens file.
indata = in_file.read()     # Stores the read data.

# print "The input file is %d bytes long." % len(indata)

# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit RETURN to continue, CRTL-C to abort."
# raw_input()

out_file = open(to_file, 'w')   # Opens file for writing.
out_file.write(indata)          # Writes stored data to new file.

print "Alright, all done."

out_file.close()    # Closes the file.
in_file.close()