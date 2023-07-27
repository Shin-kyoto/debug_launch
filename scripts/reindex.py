#!/usr/bin/env python3

import subprocess
import os
import time
import argparse
import multiprocessing

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("dir", type=str, metavar="./<relpath to zst list dirs>")
    p.add_argument("--workers", type=int, default=multiprocessing.cpu_count(), required=False, metavar="<number of workers>")
    args = p.parse_args()
    cwd = os.getcwd()
    base_dir = os.path.join(cwd, args.dir)
    dirs = [d for d in os.listdir(base_dir)]
    max_process = args.workers
    processes = set()
    for i, dir in enumerate(dirs):
        bag_dir = os.path.join(base_dir, dir)
        if not os.path.isdir(bag_dir):
            continue
        is_bag_dir = any([str(f).endswith( ".db3") for f in os.listdir(
            bag_dir) if os.path.isfile(os.path.join(bag_dir, f))])
        if not is_bag_dir:
            continue

        processes.add(subprocess.Popen(
            ['ros2', 'bag', 'reindex',  str(bag_dir)]))
        print("processing {}".format(dir))
        if len(processes) == max_process:
            finished = []
            while len(finished) == 0:
                for proc in processes:
                    if proc.poll() is not None:
                        finished.append(proc)
                if len(finished) == 0:
                    # poll every 1s to get next finished task
                    time.sleep(1)
            for finished_proc in finished:
                finished_proc.wait() # gracefully finish
                processes.remove(finished_proc)

    for proc in processes:
        proc.wait()
