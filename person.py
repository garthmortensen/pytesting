class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    def greet(self):
        return f"Hello {self.fullname()}"

    def __repr__(self):
        return f"Person, vars = {vars(self)}"
