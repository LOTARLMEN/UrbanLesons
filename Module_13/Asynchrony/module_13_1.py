import asyncio


async def start_strongman(name, power):
    for ball in range(5):
        print(f'Силач {name}, начал соревнования!')
        await asyncio.sleep(1 / power)
        print(f'Силачан {name}, поднял {ball + 1} шар!')
    print(f'Силач {name}, закончил соревнования!')


async def start_tournament():
    task = asyncio.create_task(start_strongman('Zoro', 2))
    task1 = asyncio.create_task(start_strongman('Luffy', 1.5))
    task2 = asyncio.create_task(start_strongman('Sanji', 1))
    await task
    await task1
    await task2


asyncio.run(start_tournament())
