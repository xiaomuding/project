class Foo:

    def __init__(self,name):
        self.__name = name
        print("created a father named ", name)
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name

    def bar(self):
        print("i am a class")
    def hello(self,name):
        print("my father is",self.__name)
        print("i am ",name)
'''
me = Foo("jinling")
me.bar()
me.hello("xianqiang")

me.set_name("gaili")
me.hello("xianqinag")
'''

class Doo(Foo):
    def lolo(self):
        print("i am son")
    def bar(self):
        print("i am a small class")

son = Doo("xiaoqiang");
son.lolo()
son.bar()

