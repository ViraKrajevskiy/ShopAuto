import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process
import json

count = 100000
sleep = 3
def io_b(sec):
    p_id = os.getpid()
    print(f"{p_id}--{current_process().name}--{current_thread().name}--ожидание")
    time.sleep(sleep)
    print(f"{p_id}--{current_process().name}--{current_thread().name}--ожидание законченно")

def cpu_b(k):
    p_id = os.getpid()
    print(f"{p_id}--{current_process().name}--{current_thread().name}--Начало")
    while k>0:
        k -= 1
    print(f"{p_id}--{current_process().name}--{current_thread().name}--Конец")

dsa = "package.json"

def openr(sax):
    with open('sar.json', 'r') as t:
         sax = json.load(t)
         sax = os.getpid()
         print(f"{sax}--{current_process().name}--{current_thread().name}--ожидание")
         time.sleep(sleep)
         print(f"{sax}--{current_process().name}--{current_thread().name}--ожидание законченно")
         return sax


if __name__ == '__main__':
    s_time = time.time()
    t1 = Thread(target=openr, args=(sleep,))
    t2 = Thread(target=openr, args=(sleep,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


    print( "user",s_time)


    #
    # s_time =time.time()
    # io_b(sleep)
    # io_b(sleep)
    # e_time = time.time()
    #print("time ",e_time - e_time)






