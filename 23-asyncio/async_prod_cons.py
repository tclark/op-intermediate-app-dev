import asyncio
from random import randint

N_PRODUCERS = 5
N_CONSUMERS = 2

async def produce(q):
    num  = randint(0, 5)
    for i in range(num):
        await asyncio.sleep(2)
        await q.put(i) 


async def consume(q):
    while True:
        await asyncio.sleep(1)
        val = await q.get()
        print(val)
        q.task_done()

async def main():
    q = asyncio.Queue()
    prods = [asyncio.create_task(produce(q)) for _ in range(N_PRODUCERS)]
    cons = [asyncio.create_task(consume(q)) for _ in range(N_CONSUMERS)]
    await asyncio.gather(*prods)
    await q.join()
    for c in cons:
        c.cancel()


if __name__ == '__main__':
    results = asyncio.run(main())
