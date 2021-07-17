import asyncio
from aiohttp import ClientSession

async def get_web(session, url):
        resp =  await session.get(url)
        content = await resp.text()
        return content


async def web_async_tasks():
    urls = ['https://google.com', 'https://github.io']
    async with ClientSession() as session:
        tasks = [asyncio.create_task(get_web(session, url)) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == '__main__':
    results = asyncio.run(web_async_tasks())
    for page in results:
        print(page[:50])
