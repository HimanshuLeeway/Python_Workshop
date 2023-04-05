class Sub1:
    def first(self):
        print("This is the first function from Sub1 class.")

class Sub2:
    def second(self):
        print("This is the second function from the Sub2 class.")

class Super:
    def final(self):
        print("This is the final method from the super class.")

s1 = Sub1()
s2 = Sub2()
s = Super()

s1.first()
s2.second()
s.final()
