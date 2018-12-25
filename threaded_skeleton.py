"""
Basic skeleton for running a threaded server.

The server will exit cleanly when all work is done, or after receiving a
Ctrl+C or a SIGQUIT (kill -3 <pid>) signal.
"""


import functools
import os
import random
import signal
import threading
import time


def worker(worker_num, max_jobs, shutdown_flag):
    print(f'worker {worker_num} created')
    inverse_desired_mean = 0.5

    for job_num in range(max_jobs):
        if shutdown_flag.is_set():
            print(f'worker {worker_num} detecting shutdown_flag set')
            return
        sleep_time = random.expovariate(inverse_desired_mean)
        time.sleep(sleep_time)
        print(f'worker{worker_num} has completed job #{job_num} '
              f'which took {sleep_time:.4} sec')
    print(f'worker{worker_num} has completed all jobs')


def cleanup(shutdown_flag, signum, frame):
    print(f'setting shutdown_flag on signal {signum}')
    shutdown_flag.set()


def main():
    shutdown_flag = threading.Event()
    signal.signal(signal.SIGINT, functools.partial(cleanup, shutdown_flag))
    signal.signal(signal.SIGQUIT, functools.partial(cleanup, shutdown_flag))

    print('Ctrl+C to exit')

    thread_ls = []
    for i in range(10):
        num_jobs = random.randint(1, 10)
        thread_ls.append(
            threading.Thread(target=worker, args=(i, num_jobs, shutdown_flag)))

    for thread in thread_ls:
        thread.start()

    for thread in thread_ls:
        thread.join()


if __name__ == '__main__':
    main()
