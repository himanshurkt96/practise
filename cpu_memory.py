import time

import psutil


def display(cpu_usage,memory_usage,bars):
    cpu_percent=(cpu_usage/100)
    cpu_bars='█' * int(cpu_percent* bars) + '-' * (bars- int(cpu_percent * bars))

    memory_percent = (memory_usage/100)
    memory_bars = '█' * int(memory_percent*bars) + '-' * (bars-int(memory_percent * bars))

    print(f"\rThe CPU usage: |{cpu_bars}| {cpu_usage:.2f}% ",end="")

    print(f" Memory usage: |{memory_bars}| {memory_usage:.2f}% ",end="\r")


while True:
    display(psutil.cpu_percent(),psutil.virtual_memory().percent,30)
    time.sleep(1)
