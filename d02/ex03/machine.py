#!/usr/local/bin/python3

import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
    def __init__(self):
        self.life = 10
    
    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90
        
        def description(self):
            self.description = "An empty cup?! Gimme my money back!"
            return self.description
    
    class BrokenMachineException(Exception):
        def __init__(self):
            Exception.__init__(self, "This coffee machine has to be repaired.")
    
    def repair(self):
        self.life = 10
    
    def serve(self, drink):
        if self.life == 0:
            raise self.BrokenMachineException()
        self.life -= 1
        a = random.randint(0, 1)
        d = {0:drink, 1:self.EmptyCup()}
        return d[a]

def test():
    coffee = CoffeeMachine()
    while True:
        try:
            a = coffee.serve(Tea()).__str__()
            print(a)
        except Exception as e:
            print(e)
            coffee.repair()

if __name__ == '__main__':
	test()