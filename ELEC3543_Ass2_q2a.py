import random
import threading
from threading import Thread
import time
import timeit

def thread_function(delay):
    time.sleep(delay)

def create_worker_pool(x):
    threads = []
    for i in range(1, x+1):
        delay = random.randint(1,10)
        threadName = f"Thread-{i}"
        y = Thread(target=thread_function, args=(delay,))
        threads.append(y)
        y.start()
        print(f"Worker {threadName} will sleep for {delay} seconds")
    for i, thread in enumerate(threads):
        thread.join()

if __name__ == '__main__':
    start = time.clock()
    print(timeit.timeit("create_worker_pool(10)", 
        setup="from __main__ import create_worker_pool", number=1))
    end = time.clock()
    print("Prog. Ex. Time: ", end - start)






