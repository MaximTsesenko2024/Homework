import asyncio


async def tart_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(5):
        await asyncio.sleep(10 / power)
        print(f'Силач {name} поднял {i + 1}')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament(*args):
    tour = []
    for i in args:
        tour.append(asyncio.create_task(tart_strongman(**i)))
    for i in tour:
        await i


strongmen = [{'name': 'Pasha', 'power': 3},
             {'name': 'Denis', 'power': 4},
             {'name': 'Apollon', 'power': 5}

             ]
asyncio.run(start_tournament(*strongmen))
