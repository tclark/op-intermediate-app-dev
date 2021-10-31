import asyncio

async def slow(n):
    await asyncio.sleep(1)
    return n

async def run_async_tasks(n):
    tasks = [asyncio.create_task(slow(i)) for i in range(n)]
    #results = await asyncio.gather(*tasks)
    results = await asyncio.gather(slow(1), slow(2))
    return results

if __name__ == '__main__':
    results = asyncio.run(run_async_tasks(5))
    print(results)
