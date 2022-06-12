#!/usr/local/bin/python3

class HotBeverage:
    price = 0.30
    name = "hot beverage"    
    
    def description(self):
        self.description = "Just some hot water in a cup."
        return self.description
    
    def __str__(self):
        s = "name : " + self.name + "\n"
        s += "price : " + str('%.2f' % self.price) + "\n"
        s += "description : " + self.description()
        return s

class Coffee(HotBeverage):
    def __init__(self):
        self.name = "coffee"
        self.price = 0.40

    def description(self):
        self.description = "A coffee, to stay awake."
        return self.description

class Tea(HotBeverage):
	def __init__(self):
		self.name = "tea"
	
	def description(self):
		self.description = "Just some hot water in a cup."
		return self.description


class Chocolate(HotBeverage):
	def __init__(self):
		self.name = "chocolate"
		self.price = 0.50
	
	def description(self):
		self.description = "Chocolate, sweet chocolate..."
		return self.description

class Cappuccino(HotBeverage):
	def __init__(self):
		self.name = "cappuccino"
		self.price = 0.45
	
	def description(self):
		self.description = "Un po’ di Italia nella sua tazza!"
		return self.description

def test():
    a = HotBeverage()
    b = Coffee()
    c = Tea()
    d = Chocolate()
    e = Cappuccino()
    print(a.__str__(), end="\n\n")
    print(b.__str__(), end="\n\n")
    print(c.__str__(), end="\n\n")
    print(d.__str__(), end="\n\n")
    print(e.__str__())

if __name__ == '__main__':
	test()