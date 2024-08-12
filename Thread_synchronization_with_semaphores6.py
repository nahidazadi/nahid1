import logging
import threading
import time
import random
from fastapi import FastAPI, APIRouter
from typing import List, Dict
from pydantic import BaseModel


router = APIRouter()

#ورودی دارد این ورودی می باشد
# {
#     "number_of_steps": 5
# }



class Items(BaseModel):
    number_of_steps: int
@router.post("/scenario6_1")#اجرای یک در میان تولید و مصرف کننده
def scenario1(items: Items):
    semaphore = threading.Semaphore(0)
    item = 0
    messages = []
    def consumer():
        nonlocal item
        messages.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {threading.current_thread().name}INFO Consumer is waiting")
        semaphore.acquire()
        messages.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')}{threading.current_thread().name} INFO Consumer notify: item number {item}")
    def producer():
        nonlocal item
        time.sleep(3)
        item = random.randint(0, 1000)
        messages.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {threading.current_thread().name}INFO Producer notify: item number {item}")
        semaphore.release()
    for i in range(items.number_of_steps):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    return {"messages": messages}






# توی این کد اومدم جوین هارو برداشتم فقط مصرف کننده چاپ میشه و در حال انتضار

class Items(BaseModel):
    number_of_steps: int
@router.post("/scenario6_2")#اجرای یک در میان تولید و مصرف کننده
def scenario1(items: Items):
    semaphore = threading.Semaphore(0)
    item = 0
    messages = []
    def consumer():
        nonlocal item
        messages.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {threading.current_thread().name}INFO Consumer is waiting")
        semaphore.acquire()
        messages.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')}{threading.current_thread().name} INFO Consumer notify: item number {item}")
    def producer():
        nonlocal item
        time.sleep(3)
        item = random.randint(0, 1000)
        messages.append(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {threading.current_thread().name}INFO Producer notify: item number {item}")
        semaphore.release()
    for i in range(items.number_of_steps):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)
        t1.start()
        t2.start()
        # t1.join()
        # t2.join()
    return {"messages": messages}