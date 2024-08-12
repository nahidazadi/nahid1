from typing import List
from fastapi import APIRouter
from pydantic import BaseModel
import threading
import time
import random





router = APIRouter()

class ThreadOutput(BaseModel):
    thread_number: int
    message: str
    #این کد از داخلی ترین کد شرو به حرکت به لبه ها میکند سمت چپ و راست و چاپ می کند

class MyThread(threading.Thread):
    def __init__(self, name, thread_number, lock, output_list):
        threading.Thread.__init__(self)
        self.name = name
        self.thread_number = thread_number
        self.lock = lock
        self.output_list = output_list

    def run(self):
        self.lock.acquire()
        try:
            start_message = f"---> {self.name} running, belonging to process ID {threading.get_ident()}"
            print(start_message)
            self.output_list.append(ThreadOutput(thread_number=self.thread_number, message=start_message))
            time.sleep(1)
            end_message = f"---> {self.name} over"
            print(end_message)
            self.output_list.append(ThreadOutput(thread_number=self.thread_number, message=end_message))
        finally:
            self.lock.release()

@router.post("/scenario4_1", response_model=List[ThreadOutput])
def run_threads():
    output_list = []
    lock = threading.Lock()
    start_time = time.time()

    threads = [
        MyThread(f"Thread#{i+1}", i+1, lock, output_list) for i in range(9)
    ]

    ordered_threads = []
    n = len(threads)
    center = n // 2

    for i in range(n):
        if i % 2 == 0:
            index = center - i // 2
        else:
            index = center + (i + 1) // 2
        ordered_threads.append(threads[index])

    for thread in ordered_threads:
        thread.start()

    for thread in ordered_threads:
        thread.join()

    output_list.append(ThreadOutput(thread_number=0, message=f"End\n--- {time.time() - start_time} seconds ---"))

    return output_list










#میاد از کوچک به بزرگ نخ هارو چاپ میکنه---------

class MyThread(threading.Thread):
    def __init__(self, name, thread_number, lock, output_list):
        threading.Thread.__init__(self)
        self.name = name
        self.thread_number = thread_number
        self.lock = lock
        self.output_list = output_list

    def run(self):
        self.lock.acquire()
        try:
            start_message = f"---> {self.name} running, belonging to process ID {threading.get_ident()}"
            print(start_message)
            self.output_list.append(ThreadOutput(message=start_message, thread_number=self.thread_number))
            time.sleep(1)
            end_message = f"---> {self.name} over"
            print(end_message)
            self.output_list.append(ThreadOutput(message=end_message, thread_number=self.thread_number))
        finally:
            self.lock.release()
@router.post("/scenario4_2", response_model=List[ThreadOutput])
def run_threads():
    output_list = []
    lock = threading.Lock()

    threads = [
        MyThread("Thread#1", 1, lock, output_list),
        MyThread("Thread#2", 2, lock, output_list),
        MyThread("Thread#3", 3, lock, output_list),
        MyThread("Thread#4", 4, lock, output_list),
        MyThread("Thread#5", 5, lock, output_list),
        MyThread("Thread#6", 6, lock, output_list),
        MyThread("Thread#7", 7, lock, output_list),
        MyThread("Thread#8", 8, lock, output_list),
        MyThread("Thread#9", 9, lock, output_list),
    ]

    start_time = time.time()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = f"End\n--- {time.time() - start_time} seconds ---"
    output_list.append(ThreadOutput(message=end_time, thread_number=0))

    return output_list













#میاد از بزرگ به کوچک نخ هارو چاپ میکنه---------




class MyThread(threading.Thread):
    def __init__(self, name, thread_number, lock, output_list):
        threading.Thread.__init__(self)
        self.name = name
        self.thread_number = thread_number
        self.lock = lock
        self.output_list = output_list

    def run(self):
        self.lock.acquire()
        try:
            start_message = f"---> {self.name} running, belonging to process ID {threading.get_ident()}"
            print(start_message)
            self.output_list.append(ThreadOutput(message=start_message, thread_number=self.thread_number))
            time.sleep(1)
            end_message = f"---> {self.name} over"
            print(end_message)
            self.output_list.append(ThreadOutput(message=end_message, thread_number=self.thread_number))
        finally:
            self.lock.release()

@router.post("/scenario4_3", response_model=List[ThreadOutput])
def run_threads():
    output_list = []
    lock = threading.Lock()

    threads = [
        MyThread("Thread#1", 1, lock, output_list),
        MyThread("Thread#2", 2, lock, output_list),
        MyThread("Thread#3", 3, lock, output_list),
        MyThread("Thread#4", 4, lock, output_list),
        MyThread("Thread#5", 5, lock, output_list),
        MyThread("Thread#6", 6, lock, output_list),
        MyThread("Thread#7", 7, lock, output_list),
        MyThread("Thread#8", 8, lock, output_list),
        MyThread("Thread#9", 9, lock, output_list),
    ]

    start_time = time.time()

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # مرتب‌سازی پیام‌ها بر اساس شماره‌ی نخ به صورت نزولی
    output_list.sort(key=lambda x: x.thread_number, reverse=True)

    end_time = f"End\n--- {time.time() - start_time} seconds ---"
    output_list.append(ThreadOutput(message=end_time, thread_number=0))

    return output_list
