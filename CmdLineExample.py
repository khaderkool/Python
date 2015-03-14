#!/usr/bin/python

import sys, getopt
def Usage():
	print 'test.py -i <inputfile> -o <outputfile>'
	sys.exit()
def main(argv):
	inputfile = ''
	outputfile = ''
#	while(1):
	try:
		print "len(sys.argv) " + str(len(sys.argv))
		if(len(sys.argv) != 5):
			print 'Usaage: test.py -i <inputfile> -o <outputfile>'
			sys.exit()
		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print 'test.py -i <inputfile> -o <outputfile>'
		Usage()
		sys.exit(2)
	print(argv , args)
	for opt, arg in opts:
		if opt == '-h':
			Usage()
		elif opt in ("-i", "--ifile"):
			print(" -i flag")
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg
			print(" -o flag")
		else:
			print ("Usage")
			Usage()
	print 'Input file is "', inputfile
	print 'Output file is "', outputfile

if __name__ == "__main__":
	main(sys.argv[1:])
