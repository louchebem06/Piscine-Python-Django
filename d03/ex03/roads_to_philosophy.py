#!./ex03/bin/python3

import sys, requests
from bs4 import BeautifulSoup

def roads_to_wikipedia(av, first = False, title_list = list()):
	if first and len(av) != 2:
		print("Error: arg")
		return
	if first:
		url = requests.get("https://en.wikipedia.org/wiki/" + av[1])
	else:
		url = requests.get("https://en.wikipedia.org/wiki/" + av)
	page = BeautifulSoup(url.content, 'html.parser')
	title = page.title.string.rstrip(" - Wikipedia")
	if title == "Philosophy":
		print(title)
		return
	if title in title_list:
		print("Infiny loop")
		return
	else:
		title_list.append(title)
	print(title)
	links = page.findAll('a')
	for link in links:
		if link.parent.name == "i":
			continue
		if link.string == None:
			continue
		if link.string[0:1] == "[" and link.string[-1:] == "]":
			continue
		href = link.get('href')
		if href == None:
			continue
		if not href[0:len("/wiki/")] == "/wiki/":
			continue
		name = href.split('/')
		return roads_to_wikipedia(name[len(name)-1], False, title_list)

if __name__ == '__main__':
	roads_to_wikipedia(sys.argv, True)
