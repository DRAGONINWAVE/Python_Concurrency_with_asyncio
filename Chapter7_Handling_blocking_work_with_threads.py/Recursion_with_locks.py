from threading import Lock, Thread
from typing import List

list_lock = Lock()


def sum_list(int_list: List[int]) -> int:
    print(f'Waiting to acquire lock ...')
    with list_lock:
        print(f'Acquire lock')
        if len(int_list) == 0:
            print(f'Finished summing')
            return 0

        else:
            head, *tail = int_list
            print(f'Summing rest of')
            return head + sum_list(tail)


thread = Thread(target=sum_list, args=([1, 2, 3, 4],))
thread.start()
thread.join()
