# This problem is about race conditions. When multiple threads read from
# & write to the same memory in an unpredictable way, we can get race
# conditions that produce hard to find bugs. The code below has such a race
# condition.
#Answer the following questions:
#
# 1. Before you run the code below, what do you think the value of
# racy_counter will be when it completes?
# 2. What was the actual result?
# 3. Increase max_workers to 40. Do you expect the final value of racy_counter
# to increase, decrease, or stay the same?
# 4. What was the actual result?
# 5. Explain what you've observed.
# (Disclaimer: This code is unpredictable. You'll get different results
# at different times and on different platforms.)

from concurrent.futures import ThreadPoolExecutor
from time import sleep, perf_counter
from random import randint

racy_counter = 0

def racy(i):
    global racy_counter
    sleep(randint(1, 2))
    local_count = racy_counter
    sleep(randint(1, 2))
    racy_counter = local_count + 1
    return 0

def do_racy_tasks(num):
    tasks = list(range(num))
    with ThreadPoolExecutor(max_workers=20) as ex:
        ex.map(racy, tasks)
        
def main():
    count = 500
    
    start = perf_counter()
    
    do_racy_tasks(count)
    
    finish = perf_counter()
    
    elapsed_time = round(finish - start, 2)
    
    print(f'Process finished in {elapsed_time} second(s)')
    print(f'racy_counter = {racy_counter}')

if __name__ == '__main__':
    main()
