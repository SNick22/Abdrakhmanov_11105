import asyncio
import random

int_list = [1, 2, 3, 4, 5, 6, 7, 8]
output_list = []


async def f():
    for i in int_list:
        await asyncio.sleep(random.randint(0, 20) * 0.001)
        output_list.append(i * 2)


async def g():
    for i in int_list:
        await asyncio.sleep(random.randint(0, 20) * 0.001)
        output_list.append(i * 3)


async def main():
    await asyncio.gather(f(), g())


if __name__ == '__main__':
    asyncio.run(main())
    print(output_list)
