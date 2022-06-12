#!/usr/local/bin/python3

import sys

def print_capital_city(av):
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
	if len(av) != 2:
		return
	if av[1] in states:
		print(capital_cities[states[av[1]]])
	else:
		print("Unknown state")
 
if __name__ == '__main__':
	print_capital_city(sys.argv)