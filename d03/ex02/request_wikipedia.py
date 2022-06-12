#!./ex02/bin/python3

import requests, json, dewiki, sys

def search(s):
    PARAMS = {
		"action": "query",
		"titles": s,
		"prop": "revisions",
		"rvprop": "content",
		"rvslots": "main",
		"formatversion": "2",
		"format": "json"
	}
    r = requests.get("https://fr.wikipedia.org/w/api.php", PARAMS)
    d = json.loads(r.text)
    try:
        p = d["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"]
    except:
        raise Exception("error")
    p = p.split('\n')
    if p[0][0:len("#REDIRECT")] == "#REDIRECT":
        return search(p[0].split("[")[2].strip("]"))
    else:
        return p

def request_wikipedia(av):
	if len(av) != 2:
		print("Error: arg")
		return
	try:
		p = search(av[1])
	except:
		print("Error: Not found")
		return
	f = open(av[1].replace(' ', '_') + ".wiki", "a")
	for l in p:
		f.write(dewiki.from_string(l) + "\n")
	f.close()
 
if __name__ == '__main__':
	request_wikipedia(sys.argv)
