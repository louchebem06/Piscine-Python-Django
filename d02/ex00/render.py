#!/usr/local/bin/python3

import sys, os, re
import settings

def varSettings(value):
	try:
		return getattr(settings, value)
	except:
		return None

def generate_file(nameFile):
	f = open(nameFile + ".html", "a")
	with open(nameFile + ".template", "r") as template:
		for line in template:
			moustaches = re.findall('{.*?}', line)
			for m in moustaches:
				replace = varSettings(m[1:len(m)-1])
				if replace is not None:
					line = line.replace(m, replace)
			f.write(line)
	f.close()
 
def render(av):
	if len(av) != 2:
		print("Error: Number of argument")
		return
	template = av[1].split('.')
	if (len(template) != 2 or template[1] != "template") or len(template[0]) == 0:
		print("Error: Composition name file not is name.template")
		return
	if os.path.exists(av[1]) == False:
		print("Error: " + av[1] + " don't not open")
		return
	generate_file(template[0])
 
if __name__ == '__main__':
	render(sys.argv)