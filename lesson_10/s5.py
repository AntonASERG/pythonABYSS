# Создайте три (или более) отдельных классов животных. 
# Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Fish:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def display_info(self):
        print(f"Fish name: {self.name}")
        print(f"Fish color: {self.color}")
        print("I am a fish!")

class Bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan
    
    def display_info(self):
        print(f"Bird name: {self.name}")
        print(f"Bird wingspan: {self.wingspan}")
        print("I am a bird!")

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Animal name: {self.name}")
        print(f"Animal age: {self.age}")
        print("I am an animal!")

# Создаем объекты классов
fish = Fish("Nemo", "orange")
bird = Bird("Eagle", 2.5)
animal = Animal("Lion", 10)

# Выводим информацию о каждом объекте
fish.display_info()
print()
bird.display_info()
print()
animal.display_info()
