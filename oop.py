class Cat:
    legs = 4 
    tail =True
    name : str = "tiger"


    def meow(self):
        print("meow")

    def play(self):
        print("playing")  

    def sleep(self):
            print("sleeping")


Cat1 = Cat()
Cat2 = Cat()
            
Cat1.play()

print(Cat1.legs)
print(Cat2.name)

Cat2.sleep()
Cat1.meow()
Cat1.sleep()
        