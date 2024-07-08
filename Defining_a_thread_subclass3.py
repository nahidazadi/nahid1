from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
import threading
import time

router = APIRouter()

class ThreadOutput(BaseModel):
    message: str

class MyThread(threading.Thread):
    def __init__(self, name, output_list):
        threading.Thread.__init__(self)
        self.name = name
        self.output_list = output_list

    def run(self):
        start_message = f"---> {self.name} running, belonging to process ID {threading.get_ident()}"
        self.output_list.append(ThreadOutput(message=start_message))
        time.sleep(1)
        end_message = f"---> {self.name} over"
        self.output_list.append(ThreadOutput(message=end_message))

@router.post("/scenario3_1", response_model=List[ThreadOutput])
def run_threads_scenario1():
    output_list = []

    threads = [
        MyThread("Thread#1", output_list),
        MyThread("Thread#5", output_list),
        MyThread("Thread#2", output_list),
        MyThread("Thread#6", output_list),
        MyThread("Thread#7", output_list),
        MyThread("Thread#3", output_list),
        MyThread("Thread#4", output_list),
        MyThread("Thread#8", output_list),
        MyThread("Thread#9", output_list),
    ]

    start_time = time.time()

    for thread in threads:
        thread.start()
        time.sleep(0.1)

    for thread in threads:
        thread.join()

    end_time = f"End\n--- {time.time() - start_time} seconds ---"
    output_list.append(ThreadOutput(message=end_time))

    return output_list




@router.post("/scenario3_2", response_model=List[ThreadOutput])
def run_threads_scenario2():
    output_list = []

    thread_names = ["Thread#1", "Thread#2", "Thread#3", "Thread#4", "Thread#5", "Thread#6", "Thread#7", "Thread#8", "Thread#9"]

    start_time = time.time()

    for name in thread_names:
        thread = MyThread(name, output_list)
        thread.start()
        thread.join()  # Wait for the current thread to finish before starting the next one

    total_time = f"End\n--- {time.time() - start_time} seconds ---"
    print(total_time)
    output_list.append(ThreadOutput(message=total_time))

    return output_list



@router.post("/scenario3_3", response_model=List[ThreadOutput])
def run_threads_scenario3():
    output_list = []

    thread_names = ["Thread#9", "Thread#8", "Thread#7", "Thread#6", "Thread#5", "Thread#4", "Thread#3", "Thread#2", "Thread#1"]

    start_time = time.time()

    for name in thread_names:
        thread = MyThread(name, output_list)
        thread.start()
        thread.join()  # Wait for the current thread to finish before starting the next one

    total_time = f"End\n--- {time.time() - start_time} seconds ---"
    print(total_time)
    output_list.append(ThreadOutput(message=total_time))

    return output_list
