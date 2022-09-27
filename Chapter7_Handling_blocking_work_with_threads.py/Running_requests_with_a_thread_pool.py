import time
import requests
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def get_status_code(url: str):
    response = requests.get(url)
    return response.status_code


start = time.time()


with ThreadPoolExecutor() as pool:
    urls = ['https://www.example.com'for _ in range(1000)]
    results = pool.map(get_status_code, urls)
    for result in results:
        print(result)

end = time.time()
print(f'finished requestes in {end-start:.4f} second(s)')
