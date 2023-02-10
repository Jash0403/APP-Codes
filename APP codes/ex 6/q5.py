import time
from threading import *

ThreadCount = 0


def req_thread(num):
    if num <= 0:
        return 0
    req_thread(num-1)
    print(f'Hello from Thread {num+1}! I am Thread {num}')


t = time.time()

thl = Thread(target=req_thread, args=(20, ))
thl.start()
thl.join()
print(" Total time taking by threads is :", time.time() - t)
