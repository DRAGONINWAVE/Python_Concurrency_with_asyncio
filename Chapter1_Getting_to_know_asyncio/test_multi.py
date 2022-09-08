import threading 
import time


def print_loop(n:int):
    a = []
    for i in range(n):
        a.append(str(i))

def loop_no_threading():
    print_loop(10000000)
    print_loop(10000000)

def loop_with_threads():
    one_million = threading.Thread(target=print_loop,args=(10000000,))
    one_trillion = threading.Thread(target=print_loop,args=(10000000,))

    one_million.start()
    one_trillion.start()

    one_million.join()
    one_trillion.join()

start = time.time()

loop_no_threading()

end = time.time()

print(f'no_threading run time is {end-start:.4f} seconds')

start1 = time.time()

loop_with_threads()

end1 = time.time()

print(f'with_threading run time is {end1-start1:.4f} seconds')



