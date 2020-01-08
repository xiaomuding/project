import threading
import time
def test(x,y):
    print("***",x*y)
    time.sleep(10)

threads = []
for i in range(10):
    threads.append(threading.Thread(target=test,args = (5,2)))

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()