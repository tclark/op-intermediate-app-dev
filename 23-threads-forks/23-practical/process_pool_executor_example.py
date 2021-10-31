# concurrent.futures.ProcessPoolExecutor is an alternative to the
# multiprocessing module.

from concurrent.futures import ProcessPoolExecutor
from time import perf_counter, sleep

def sleeping(secs):
    print(f'Going to sleep for {secs} second(s)')
    sleep(secs)
    return f'Woke up after {secs} second(s)'

def main():
    start = perf_counter()

    with ProcessPoolExecutor() as ex:
        secs = [_ for _ in reversed(range(1, 6))]
        ex.map(sleeping, secs)
        

    finish = perf_counter()
    
    elapsed_time = round(finish - start, 2)
    
    print(f'Process finished in {elapsed_time} second(s)')

if __name__ == '__main__':
    main()
