import multiprocessing as mp
import time
import psutil


def task(burn_time):
    counter = 0
    now = time.time()

    while time.time() < now + burn_time:
        counter += 1


if __name__ == '__main__':
    cpu_count = mp.cpu_count()
    num_processes = cpu_count - 2
    processes = []
    process_last_time_s = 60

    for _ in range(num_processes):
        process = mp.Process(target=task, args=(process_last_time_s,))
        process.daemon = True
        processes.append(process)
        process.start()

    parent = psutil.Process()
    if parent.parent() == None:
        print("main")

    for child in parent.children():
        child.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)

    for process in processes:
        process.join()

