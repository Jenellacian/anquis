    class Person:
        def __init__(self, name):
            self.name = name

        def say_hi(self):
            print(f"Hello, my name is {self.name}")

    # Creating an instance of Person
    p = Person("Nikhil")
    p.say_hi()  # Output: Hello, my name is Nikhil
    