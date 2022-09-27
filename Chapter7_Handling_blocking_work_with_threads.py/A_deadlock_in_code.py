from threading import Lock, Thread
import time

lock_a = Lock()
lock_b = Lock()


def a():
    with lock_a:
        print(f'Acquire lock for a from method a!')
        time.sleep(1)
        with lock_b:
            print('Acquired both locks from method a!')


def b():
    with lock_b:
        print(f'Acquired lock b from method b!')
        with lock_a:
            print('Acquired both locks from method b!')


thread_1 = Thread(target=a)
thread_2 = Thread(target=b)
thread_1.start()
thread_2.start()
thread_1.join()
thread_2.join()
