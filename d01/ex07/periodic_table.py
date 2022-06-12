#!/usr/local/bin/python3

def info(str):
	str = str.split(',')
	name = str[0].split("=")[0].strip()
	position = int(str[0].split("=")[1].split(":")[1].strip())
	number = str[1].split(":")[1].strip()
	small = str[2].split(":")[1].strip()
	molar = str[3].split(":")[1].strip()
	electron = str[4].split(":")[1].strip()
	return({"name" : name,
         	"position" : position,
          	"number" : number,
           	"small" : small,
            "molar" : molar,
            "electron" : electron})

def base_html(f):
	f.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Periodic table</title>
	<style>
		table { border-collapse: collapse; }
		table tr, table td { border: solid 1px black; }
		table td { padding:10px }
		h4 { text-align: center }
	</style>
</head>
<body>
	<table>
		<tr>
""")

def end_html(f):
	f.write("""		</tr>
	</table>     
</body>
</html>""")

def print_case(f, e):
	f.write('		<td>\n')
	f.write('			<h4>' + str(e["name"]) + '</h4>\n')
	f.write('			<ul>\n				<li>No ' + e["number"] + '</li>\n')
	f.write('				<li>' + e["small"] + '</li>\n')
	f.write('				<li>' + e["molar"] + '</li>\n')
	f.write('				<li>' + e["electron"] + ' electron</li>\n			</ul>\n')
	f.write('		</td>\n')

def print_table(f, elements):
    item = 0
    col = 0
    for element in elements:
        while item != element["position"]:
            f.write('		<td>\n		</td>\n')
            item += 1
            if item == 18 and col != 6:
                item = 0
                col += 1
                f.write('		</tr>\n		<tr>\n')
        print_case(f, element)
        item += 1
        if item == 18 and col != 6:
            item = 0
            col += 1
            f.write('		</tr>\n		<tr>\n')

def create_file(elements):
    f = open("index.html", "a")
    base_html(f)
    print_table(f, elements)
    end_html(f)
    f.close()

def periodic_table():
	elements = list()
	with open("periodic_table.txt", "r") as f:
		for line in f:
			elements.append(info(line))
	create_file(elements)
 
if __name__ == '__main__':
	periodic_table()
