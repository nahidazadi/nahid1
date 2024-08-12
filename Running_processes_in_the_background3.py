from fastapi import FastAPI, APIRouter
from typing import List, Dict
import multiprocessing
import time
import uvicorn


router = APIRouter()
#سناریو اولللللللللللللل
#اگر هر دوتا دایمنت ها فالز باشن خروجی مثل خروجی پاینی توی تمرین می شود

def foo(output_queue, start, end):
    name = multiprocessing.current_process().name
    output_queue.put(f"Starting {name}")
    for i in range(start, end):
        output_queue.put(f'---> {i}')
        time.sleep(1)
    output_queue.put(f"Exiting {name}")

@router.post("/scenario2_3_1", response_model=List[Dict[str, str]])
def run_processes():
    output_queue = multiprocessing.Queue()

    # Define processes
    background_process = multiprocessing.Process(
        name='background_process', target=foo, args=(output_queue, 0, 5)
    )
    background_process.daemon = False  # Set to True for testing

    NO_background_process = multiprocessing.Process(
        name='NO_background_process', target=foo, args=(output_queue, 5, 10)
    )
    NO_background_process.daemon = False  # Set to False for testing

    processes = [background_process, NO_background_process]

    # Start and join only non-daemon processes
    for process in processes:
        if not process.daemon:
            process.start()

    for process in processes:
        if not process.daemon:
            process.join()

    # Collect results from the queue
    results = []
    while not output_queue.empty():
        result = output_queue.get()
        results.append({"process_output": result})

    return results





#سناریو دومممممممممممممممممم

#توی این سناریو از یک تا 5 چاپ نمی شوند بقیه چاپ میشن

def foo(output_queue, start, end):
    name = multiprocessing.current_process().name
    output_queue.put(f"Starting {name}")
    for i in range(start, end):
        output_queue.put(f'---> {i}')
        time.sleep(1)
    output_queue.put(f"Exiting {name}")

@router.post("/scenario2_3_2", response_model=List[Dict[str, str]])
def run_processes():
    output_queue = multiprocessing.Queue()

    # Define processes
    background_process = multiprocessing.Process(
        name='background_process', target=foo, args=(output_queue, 0, 5)
    )
    background_process.daemon = True  # Set to True for testing

    NO_background_process = multiprocessing.Process(
        name='NO_background_process', target=foo, args=(output_queue, 5, 10)
    )
    NO_background_process.daemon = False  # Set to False for testing

    processes = [background_process, NO_background_process]

    # Start and join only non-daemon processes
    for process in processes:
        if not process.daemon:
            process.start()

    for process in processes:
        if not process.daemon:
            process.join()

    # Collect results from the queue
    results = []
    while not output_queue.empty():
        result = output_queue.get()
        results.append({"process_output": result})

    return results




#سناریو سوممممممممممممممم
#از صفر تا چهار چاپ می شود بقیه چاپ نمی شوند اگر هر دوتا را فالز کنیم لیست خالی تحویل میدهد

def foo(output_queue, start, end):
    name = multiprocessing.current_process().name
    output_queue.put(f"Starting {name}")
    for i in range(start, end):
        output_queue.put(f'---> {i}')
        time.sleep(1)
    output_queue.put(f"Exiting {name}")

@router.post("/scenario2_3_3", response_model=List[Dict[str, str]])
def run_processes():
    output_queue = multiprocessing.Queue()

    # Define processes
    background_process = multiprocessing.Process(
        name='background_process', target=foo, args=(output_queue, 0, 5)
    )
    background_process.daemon = False  # Set to True for testing

    NO_background_process = multiprocessing.Process(
        name='NO_background_process', target=foo, args=(output_queue, 5, 10)
    )
    NO_background_process.daemon = True  # Set to False for testing

    processes = [background_process, NO_background_process]

    # Start and join only non-daemon processes
    for process in processes:
        if not process.daemon:
            process.start()

    for process in processes:
        if not process.daemon:
            process.join()

    # Collect results from the queue
    results = []
    while not output_queue.empty():
        result = output_queue.get()
        results.append({"process_output": result})

    return results





