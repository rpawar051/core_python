# A python program to invoke a method on an objects without knowing the type (or class) of the object.
# duck typing example
# Duck class contains talk() methods
class Duck:
    def talk(self):
        print("Quick Quick !!")

# human class contains talk() methods 
class Human:
    def talk(self):
        print("Hello hi")

# this methods accepts an objects and calls talk() methods
def call_talk(obj):
    print("-"*50)
    print(obj)
    obj.talk()
    print("-"*50)
    

# call call_talk() method and pass an object 
# depending on type of object, talk() method is executed
x = Duck()
call_talk(x)
x = Human()
call_talk(x)

