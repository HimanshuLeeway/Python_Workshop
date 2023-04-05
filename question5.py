
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        return self.name

class B:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def details(self):
        return self.name

class C(A, B):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
      
    def get_details(self):
        return self.name

c = C("John", 25, 123)

print(c.get_details())  # Output: John
