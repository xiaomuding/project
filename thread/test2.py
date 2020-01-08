# from multiprocessing import Semaphore

from threading import Thread,Semaphore,current_thread
import time,random

sm = Semaphore(10)

def go_wc():
    sm.acquire()
    print('%s 上厕所ing' %current_thread().getName())
    time.sleep(10)
    sm.release()

if __name__ == '__main__':
    for i in range(23):
        t=Thread(target=go_wc)
        t.start()