from random import random

from fastapi import FastAPI, APIRouter
from typing import List, Dict
import multiprocessing
import uvicorn
from typing import List, Dict
import multiprocessing
router = APIRouter()
from typing import List, Dict
import multiprocessing
from pydantic import BaseModel
from typing import List
import random


#صففففففففففففففففف



def myFunc(i, output):
    output_str = f'calling myFunc from process n°: {i}\n'
    for j in range(i):
        output_str += f'output from myFunc is : {j}\n'
    output.put(output_str)

@router.post("/scenario2_1_1", response_model=List[Dict[str, str]])
def run_processes():
    output = multiprocessing.Queue()

    processes = []
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i, output))
        processes.append(process)
        process.start()
        process.join()

    results = []
    while not output.empty():
        result = output.get()
        lines = result.strip().split("\n")
        for line in lines:
            results.append({"process_output": line})

    return results



#دومممممممممممممممممممممممممممم



# تابعی که توسط پروسه‌ها اجرا می‌شود
def myFunc(i, output):
    output_str = f'calling myFunc from process n°: {i}\n'
    for j in range(i):
        output_str += f'output from myFunc is : {j}\n'
    output.put(output_str)

# مسیر API برای اجرای پروسه‌ها و بازگرداندن نتایج
@router.post("/scenario2_1_2", response_model=List[Dict[str, str]])
def run_processes():
    output = multiprocessing.Queue()

    processes = []
    for i in range(6):
        process = multiprocessing.Process(target=myFunc, args=(i, output))
        processes.append(process)
        process.start()

    # منتظر ماندن برای تکمیل همه پروسه‌ها
    for process in processes:
        process.join()

    results = []
    while not output.empty():
        result = output.get()
        lines = result.strip().split("\n")
        for line in lines:
            results.append({"process_output": line})

    # شافل کردن نتایج برای تصادفی بودن خروجی
    random.shuffle(results)

    return results


#سوممممممممممممممممممممممممممممممم

#توی این سناریو اومدم تعداد رو از 6 به 4 تبدیل کردم

def myFunc(i, output):
    output_str = f'calling myFunc from process n°: {i}\n'
    for j in range(i):
        output_str += f'output from myFunc is : {j}\n'
    output.put(output_str)

@router.post("/scenario2_1_3", response_model=List[Dict[str, str]])
def run_processes():
    output = multiprocessing.Queue()

    processes = []
    for i in range(4):
        process = multiprocessing.Process(target=myFunc, args=(i, output))
        processes.append(process)
        process.start()
        process.join()

    results = []
    while not output.empty():
        result = output.get()
        lines = result.strip().split("\n")
        for line in lines:
            results.append({"process_output": line})

    return results
















































#
# #خروجی مطابق با خروجی داده شده در تمرین
# def myFunc(i, output_dict):
#     output_str = f'calling myFunc from process n°: {i}\n'
#     for j in range(i):
#         output_str += f'output from myFunc is : {j}\n'
#     output_dict[i] = output_str
#
# @router.post("/run-processes", response_model=List[Dict[str, str]])
# def run_processes():
#     manager = multiprocessing.Manager()
#     output_dict = manager.dict()
#
#     processes = []
#     for i in range(6):
#         process = multiprocessing.Process(target=myFunc, args=(i, output_dict))
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
#     results = []
#     for i in range(6):
#         result = output_dict.get(i, "")
#         lines = result.strip().split("\n")
#         for line in lines:
#             results.append({"process_output": line})
#
#     return results
#
#
#
#
#
# #این میاد از بزرگ به کوچیک برام چاپ میکنه
#
# def myFunc(i, output_dict):
#     output_str = f'calling myFunc from process n°: {i}\n'
#     for j in range(i):
#         output_str += f'output from myFunc is : {j}\n'
#     output_dict[i] = output_str
#
# @router.post("/run-processes1", response_model=List[Dict[str, str]])
# def run_processes():
#     manager = multiprocessing.Manager()
#     output_dict = manager.dict()
#
#     processes = []
#     for i in range(6):
#         process = multiprocessing.Process(target=myFunc, args=(i, output_dict))
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
#     results = []
#     for i in sorted(output_dict.keys(), reverse=True):
#         result = output_dict[i]
#         lines = result.strip().split("\n")
#         for line in lines:
#             results.append({"process_output": line})
#
#     return results
#
#
#
#
#
# def myFunc(i, output_dict):
#     output_str = f'calling myFunc from process n°: {i}\n'
#     for j in range(i):
#         output_str += f'output from myFunc is : {j}\n'
#     output_dict[i] = output_str
#
# @router.post("/run-processes3", response_model=List[Dict[str, str]])
# def run_processes():
#     manager = multiprocessing.Manager()
#     output_dict = manager.dict()
#
#     processes = []
#     for i in range(6):
#         process = multiprocessing.Process(target=myFunc, args=(i, output_dict))
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
#     results = []
#     for i in output_dict.keys():
#         result = output_dict[i]
#         lines = result.strip().split("\n")
#         for line in lines:
#             results.append({"process_output": line})
#
#     random.shuffle(results)  # مخلوط کردن خروجی‌ها به صورت تصادفی
#
#     return results
#
#
#
#
#
# #این هم اومدم از دیکشنری استفاده کرده ام کلید و مقدار ولد هارو شافل می کند به صورت رندم
#
# def myFunc(i, output_dict):
#     output_str = f'calling myFunc from process n°: {i}\n'
#     for j in range(i):
#         output_str += f'output from myFunc is : {j}\n'
#     output_dict[i] = output_str
#
# @router.post("/run-processes4", response_model=List[Dict[str, str]])
# def run_processes():
#     manager = multiprocessing.Manager()
#     output_dict = manager.dict()
#
#     processes = []
#     for i in range(6):
#         process = multiprocessing.Process(target=myFunc, args=(i, output_dict))
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()
#
#     results = []
#     keys = list(output_dict.keys())
#     random.shuffle(keys)  # مخلوط کردن کلیدها به صورت تصادفی
#
#     for i in keys:
#         result = output_dict[i]
#         lines = result.strip().split("\n")
#         for line in lines:
#             results.append({"process_output": line})
#
#     return results
#
#


