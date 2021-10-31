# Answer the questions below
# 1. What is concurrency?
# 2. What is the difference between CPU bound & I/O bound?
# 3. When the following code is executed, what is happening?
# 4. The Thread object s constructed below with two arguments. What are these
#    arguments & their purpose?
# 5. What does the threading function start do?
# 6. What does the threading function join do?
##########

from threading import Thread
from time import perf_counter, sleep

def sleeping(secs):
    print(f'Going to sleep for {secs} second(s)')
    sleep(secs)
    print(f'Woke up after {secs} second(s)')

def main():
    start = perf_counter()

    threads = [Thread(target=sleeping, args=[5]) for _ in range(5)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    finish = perf_counter()
    
    elapsed_time = round(finish - start, 2)
    
    print(f'Process finished in {elapsed_time} second(s)')

if __name__ == '__main__':
    main()
