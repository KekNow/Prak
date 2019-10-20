import time
import os
import librosa
import numpy
from concurrent.futures import ProcessPoolExecutor


def extract_mfcc(dir, dest, files):
    for j in files:
        x, sr = librosa.load(dir + "\\" + j)
        mfcc_array = librosa.feature.mfcc(x, sr)
        with open(dest + "\\" + j[:-4] + ".txt", 'w') as f:
            numpy.savetxt(f, mfcc_array)


if __name__ == '__main__':
    start_time = time.perf_counter()
    path = "Tests_Audio2"
    destination = path + "_RESULTS_PROCESSES"
    with ProcessPoolExecutor(4) as pool:
        for way, folders, files in os.walk(path):
            dest = destination + "\\" + way[len(path)+1:]
            os.mkdir(dest)
            if files:
                pool.submit(extract_mfcc, way, dest, files)
    with open("Results.txt", 'a') as res:
        timer = "Working time, processes: " + str(time.perf_counter() - start_time) + '\n'
        res.write(timer)