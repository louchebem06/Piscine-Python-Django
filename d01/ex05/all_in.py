#!/usr/local/bin/python3

import sys

def check(arg, argOrigin):
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	d = dict()
	for k, v in states.items():
		d[k] = capital_cities[v]
	for k, v in d.items():
		if arg == k or arg == v:
			print(k + " is the capital of " + v)
			return
	print(argOrigin + " is neither a capital city nor a state")

def print_all_in(av):
	if len(av) != 2:
		return
	av = av[1].split(",")
	for str in av:
		str = str.strip()
		if len(str) == 0:
			continue
		check(str.title(), str)
 
if __name__ == '__main__':
	print_all_in(sys.argv)