class A:
    def __init__(self,name):
        self.name = name
    def show(self):
        print("i am ", self.name)

a =A("hello")

print(dir(a))