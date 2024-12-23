import argparse
import sys
from infection import infect

PROGRAM_VERSION = "1.0.0"

def parse_args():

	parser = argparse.ArgumentParser(description="stockholm arguments")
	parser.add_argument('-v', '--version', action='version', version=f"%(prog)s {PROGRAM_VERSION}", help="Show the program version and exit.", default=False)
	parser.add_argument('-r', '--reverse', help='Reverse infection', action='store_true', default=False)
	parser.add_argument('-s', '--silent', help='Silence terminal output', action='store_true', default=False)
	parser.add_argument('key', nargs='?', help="16 characters key provided by the user.", default=None)
	args = parser.parse_args()

	if not args.key:
		parser.error("Requires a 16 characters key as argument")
	
	return args

def main():
	args = parse_args()

	infect(args)



if __name__ == "__main__":
	main()