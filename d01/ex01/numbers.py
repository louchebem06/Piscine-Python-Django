#!/usr/local/bin/python3

def print_number_of_file():
	with open("numbers.txt", "r") as f:
		for line in f:
			for c in line:
				if c != ',':
					print(c, end='')
				else:
					print()


if __name__ == '__main__':
	print_number_of_file()