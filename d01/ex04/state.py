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
	capital_cities = {v:k for k, v in capital_cities.items()}
	states = {v:k for k, v in states.items()}
	if av[1] in capital_cities:
		print(states[capital_cities[av[1]]])
	else:
		print("Unknown capital city")
 
if __name__ == '__main__':
	print_capital_city(sys.argv)