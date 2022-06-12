#!/usr/local/bin/python3

class Intern:
    def __init__(self, Name = "My name? I’m nobody, an intern, I have no name."):
        self.Name = Name
    
    def __str__(self):
        return self.Name
    
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."
        
    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")
    
    def make_coffee(self):
        return Intern.Coffee()

def test():
    noName = Intern()
    Mark = Intern("Mark")
    print(noName.__str__())
    print(Mark.__str__())
    coffee = Mark.make_coffee()
    print(coffee.__str__())
    try:
        noName.work()
    except Exception as e:
        print(e)

if __name__ == '__main__':
	test()