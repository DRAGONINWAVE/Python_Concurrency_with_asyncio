import time
import threading
#from urllib import response
import requests

def read_example() -> None:
    response = requests.get('https://www.baidu.com/')
    print(response.status_code)

thread_1 = threading.Thread(target=read_example)
thread_2 = threading.Thread(target=read_example)

thread_start = time.time()

thread_1.start()
thread_2.start()

print('All threads running!')

thread_1.join()
thread_2.join()

thread_end = time.time()

print(f'Running with threads took {thread_end - thread_start:.4f} seconds')