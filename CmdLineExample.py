#!/usr/bin/python

# import comand line related libraries

import sys, getopt

#helper functions

def Usage():
	print 'test.py -i <inputfile> -o <outputfile>'
	sys.exit()

# main function
def main(argv):
	#start caring for exceptions
	try:
		print "len(sys.argv) " + str(len(sys.argv))
		# make sure that we have 5 args 1)filename 2) -i 3) filename 4) -o 5) filename
		if(len(sys.argv) != 5):
			print 'Usaage: test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		Usage()
		sys.exit(2)
#	print(argv , args)
	for opt, arg in opts:
		if opt == '-h':
			Usage()
		elif opt in ("-i", "--ifile"):
			print("input file path: " + arg)
			#inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
			print("Output file path: " + arg)
		else:
			print ("Usage")
			Usage()

# lets wait for our main function

if __name__ == "__main__":
	main(sys.argv[1:])
