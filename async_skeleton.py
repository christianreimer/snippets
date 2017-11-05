"""
Basic skeleton for running an asyncio server.

The server will exit cleanly when all work is done, or after receiving a
Ctrl+C or a SIGQUIT (kill -3 <pid>) signal.
"""


import asyncio
import signal
import random


async def worker1(max_jobs=100):
    for _ in range(max_jobs):
        sleep_time = random.expovariate(1 / 2)
        await asyncio.sleep(sleep_time)
        print(f'worker1 has completed a job which took {sleep_time:.2} sec')
    print('worker1 has completed all jobs')


async def worker2(max_jobs=100):
    for _ in range(max_jobs):
        sleep_time = random.expovariate(1 / 2)
        await asyncio.sleep(sleep_time)
        print(f'worker2 has completed a job which took {sleep_time:.2} sec')
    print('worker2 has completed all jobs')


def cleanup():
    print('Canceling outstanding tasks')
    for task in asyncio.Task.all_tasks():
        task.cancel()


def main():
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, cleanup)
    loop.add_signal_handler(signal.SIGQUIT, cleanup)

    print('Ctrl+C to exit')

    try:
        loop.run_until_complete(asyncio.wait((worker1(), worker2())))
    except asyncio.CancelledError:
        pass

    loop.close()


if __name__ == '__main__':
    main()
