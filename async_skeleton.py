"""
Basic skeleton for running an asyncio server.

The server will exit cleanly when all work is done, or after receiving a
Ctrl+C or a SIGQUIT (kill -3 <pid>) signal.
"""


import asyncio
import signal
import random


def make_worker(worker_num, max_jobs=100):
    async def worker():
        inverse_desired_mean = 0.5
        for _ in range(max_jobs):
            sleep_time = random.expovariate(inverse_desired_mean)
            await asyncio.sleep(sleep_time)
            print(f'worker{worker_num} has completed a job '
                  f'which took {sleep_time:.4} sec')
        print('worker1 has completed all jobs')
    return worker()


def cleanup():
    print('Canceling outstanding tasks')
    for task in asyncio.Task.all_tasks():
        task.cancel()


def main():
    loop = asyncio.get_event_loop()
    loop.add_signal_handler(signal.SIGINT, cleanup)
    loop.add_signal_handler(signal.SIGQUIT, cleanup)

    workers = []
    for i in range(10):
        workers.append(make_worker(i))

    print('Ctrl+C to exit')

    try:
        loop.run_until_complete(asyncio.wait(workers))
    except asyncio.CancelledError:
        pass

    loop.close()


if __name__ == '__main__':
    main()

