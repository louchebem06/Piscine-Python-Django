#!/usr/local/bin/python3

from shutil import which
from local_lib.path import Path

def my_program():
	p = Path("./abcd").mkdir_p()
	f = open(p + "/file", "a")
	f.write("line")
	f.close()
	with open(p + "/file", "r") as f:
		for l in f:
			print(l)
 
if __name__ == '__main__':
	my_program()