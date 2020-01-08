from threading import Thread


class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.setName(name)
        print("i am a thread. my name is ", self.getName())
        # super(MyThread, self).__init__()

    def run(self):
        # write this thread task
        pass


if __name__ == '__main__':
    thread123 = MyThread("saisai")
    thread2 = MyThread("xianqiang")
    thread123.start()
    thread2.start()
    thread123.join()
    thread2.join()

