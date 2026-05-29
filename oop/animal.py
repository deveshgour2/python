class animal:
    def speak(self):
        print("animal sounds")

class dog(animal):
    def speak(self):
        print("Dog Barks")
    
class cat(animal):
    def speak(self):
        print("Cat Meow")

d = dog()
c = cat()

d.speak()
c.speak()
