# Answer the questions below
#
#   1. What is parallelism?
#   2. When the following cell is executed, what is happening?
#   3. What does the multiprocessing function start do?
#   4. What does the multiprocessing function join do?
##########


from multiprocessing import Process
from time import perf_counter, sleep

def sleeping(secs):
    print(f'Going to sleep for {secs} second(s)')
    sleep(secs)
    print(f'Woke up after {secs} second(s)')

def main():     
    start = perf_counter()

    processes = [Process(target=sleeping, args=[5]) for _ in range(5)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    finish = perf_counter()
    
    elapsed_time = round(finish - start, 2)
    
    print(f'Process finished in {elapsed_time} second(s)')

if __name__ == '__main__':
    main()
