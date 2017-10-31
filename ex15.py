# from sys import argv    # imports argt module
#
# script, filename = argv     # creates a variable to store file name
#
# txt = open(filename)    # opens the file
#
# print "Here's your file %r: " % filename
# print txt.read()    # reads the file

print "Type the file name again:"
file_again = raw_input("> ")    # takes input from user

txt_again = open(file_again)    # opens the file

print  txt_again.read()     # reads the file
