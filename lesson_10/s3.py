class Person:
    def __init__(self, first_name, last_name, age):
        self._first_name = first_name
        self._last_name = last_name
        self._age = age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    # свойство для получения текущего возраста
    @property
    def age(self):
        return self._age

person = Person("Иван", "Иванов", 30)
print(person.full_name())  # Выводит "Иван Иванов"
print(person.age)  # Выводит 30

person.birthday()
print(person.age)  # Выводит 31
