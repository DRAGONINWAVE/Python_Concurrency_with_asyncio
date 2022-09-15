import time
#from urllib import response
import requests

def read_example() -> None:
    response = requests.get('https://www.baidu.com/')
    print(response.status_code)

sync_start = time.time()

read_example()
read_example()

sync_end  =time.time()

print(f'Running synchrously took {sync_end - sync_start:.4f} seconds.')