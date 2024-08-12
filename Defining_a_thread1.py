from typing import List
import uvicorn
from fastapi import FastAPI, HTTPException, Request, BackgroundTasks,APIRouter
from pydantic import BaseModel
import threading
import time

router=APIRouter()

class ThreadOutput(BaseModel):
    thread_number: int
    message: str





def my_func(thread_number):
    return f'my_func called by thread N°{thread_number}'


@router.post("/scenario1_1", response_model=List[ThreadOutput])
def scenario1():
    outputs = []

    def my_func_wrapper(thread_number):
        message = my_func(thread_number)
        outputs.append(ThreadOutput(thread_number=thread_number, message=message))

    threads = []
    for num in range(10):
        t = threading.Thread(target=my_func_wrapper, args=(num,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Sort outputs by thread_number
    outputs.sort(key=lambda x: x.thread_number)

    return outputs


@router.post("/scenario1_2", response_model=List[ThreadOutput])
def scenario2():
    outputs = []

    def my_func_wrapper(thread_number):
        message = my_func(thread_number)
        if thread_number % 2 == 0:
            outputs.append(ThreadOutput(thread_number=thread_number, message=message))
        else:
            outputs.insert(0, ThreadOutput(thread_number=thread_number, message=message))

    threads = []
    for num in range(10):
        t = threading.Thread(target=my_func_wrapper, args=(num,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return outputs


@router.post("/scenario1_3", response_model=List[ThreadOutput])
def scenario3():
    outputs = []

    def my_func_wrapper(thread_number):
        message = my_func(thread_number)
        outputs.append(ThreadOutput(thread_number=thread_number, message=message))

    threads = []
    for num in sorted(range(10), reverse=True):
        t = threading.Thread(target=my_func_wrapper, args=(num,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return outputs