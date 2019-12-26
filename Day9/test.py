from concurrent.futures import ThreadPoolExecutor
from threading import Lock

pool = ThreadPoolExecutor(10)
locker = Lock()


def task():
    locker.acquire()
    print('Hello!')
    locker.release()


for i in range(50):
    pool.submit(task)
