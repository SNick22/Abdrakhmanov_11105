import asyncio
from queue import Queue
from aioconsole import ainput

queue = Queue()


async def enter():
    while True:
        queue.put(await ainput())


async def printing():
    while True:
        await asyncio.sleep(3)
        if not queue.empty():
            print(queue.get())
        else:
            continue


async def main():
    await asyncio.gather(enter(), printing())


if __name__ == '__main__':
    asyncio.run(main())
