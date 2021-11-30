class Animal:
    def __init__(self, name, color, legs) -> None:
        self.name = name
        self.color = color
        self.legs = legs

class Cat(Animal):
    def purr(self):
        print('Purr...')

class Dog(Animal):
    def bark(self):
        print('Woof!')

felix = Cat("Ninny", "ginger", 4)
rover = Cat('Shula', "dog-colored", 4)
stumpy = Dog('Leo', "brown", 4)

stumpy.bark()
felix.purr()
