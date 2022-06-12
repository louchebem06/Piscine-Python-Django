#!/usr/local/bin/python3

import sys
import antigravity

def geohashing(av):
	if len(av) != 4:
		print("Error: nb of argument")
		return
	latitude = av[1].split('.')
	longitude = av[2].split('.')
	if len(latitude) != 2 or len(longitude) != 2:
		print("Error: coordinate")
		return
	for l in latitude:
		if not l.lstrip("-").isdigit():
			print("Error: coordinate")
			return
	for l in longitude:
		if not l.lstrip("-").isdigit():
			print("Error: coordinate")
			return
	antigravity.geohash(float(av[1]), float(av[2]), str.encode(av[3]))
 
if __name__ == '__main__':
	geohashing(sys.argv)