class Parent:
    hair_color = "brown"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("German")


