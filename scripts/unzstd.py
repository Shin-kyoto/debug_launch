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
    zstd_files = []
    for i, dir in enumerate(dirs):
        zstd_dir = os.path.join(base_dir, dir)
        if not os.path.isdir(zstd_dir):
            continue
        files = [os.path.join(zstd_dir, f) for f in os.listdir(zstd_dir) if os.path.isfile(os.path.join(zstd_dir, f))]
        if len(files) == 0:
            continue
        zstd_file = files[0]
        if not str(zstd_file).endswith(".zst"):
            continue
        zstd_file = os.path.join(dir, zstd_file)
        zstd_files.append(zstd_file)
        processes.add(subprocess.Popen(['unzstd', zstd_file]))
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

    for zstd_file in zstd_files:
        db3_file = zstd_file.replace(".zst", '')
        if os.path.exists(db3_file):
            proc = subprocess.Popen(['mv', db3_file, base_dir])
            proc.wait()
