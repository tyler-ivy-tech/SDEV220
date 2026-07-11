from multiprocessing import Process
import os
from datetime import datetime
from time import sleep
from random import random

def print_time_process(wait_time):
    print(f"Process {os.getpid()} started.")
    sleep(wait_time)
    print(f"Process {os.getpid()}: {datetime.now()}")

if __name__ == "__main__":
    for i in range(3):
        wait_time = random()
        p = Process(target=print_time_process, args=(wait_time,))
        p.start()

    print("All processes started.")