class Dog:
    species = "Canis familiaris"
    def __init__(self,name,age, breed):
        species = "Canis familiaris"
        self.name = name
        self.age = age
        self.breed = breed

    def description(self):
        return f"{self.name} is {self.age} years old"
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        return f"{self.name} says {sound}"

class ShihTzu(Dog):
    def __init__(self, name, age):
        super().__init__(name, age, breed = "ShihTzu")
    def speak(self,sound ="Au"):
        return super().speak(sound)
        #return f"{self.name} says {sound}"
class GoldenRt(Dog):
    def __init__(self, name, age):
        super().__init__(name, age, breed = "ShihTzu")
    def speak(self,sound ="Bark"):
        return f"{self.name} barks: {sound}"
    
lupi = ShihTzu("Lupi",7)
print(lupi.speak("Grr"))
print(lupi.species)
print(isinstance(lupi, Dog))
jose = GoldenRt("Jose",6)
print(jose.speak())