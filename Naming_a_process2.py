from fastapi import FastAPI, APIRouter
from typing import List, Dict
import multiprocessing
import time
import uvicorn


router = APIRouter()

def myFunc(sleep_time, output_list):
    name = multiprocessing.current_process().name
    output_str = f"Starting  {name}"
    output_list.append({"process_output": output_str})
    time.sleep(sleep_time)
    output_str = f"Exiting  {name}"
    output_list.append({"process_output": output_str})

@router.post("/scenario2_2_1", response_model=List[Dict[str, str]])
def run_processes():
    manager = multiprocessing.Manager()
    output_list = manager.list()

    # Start processes in the desired order
    process_with_name = multiprocessing.Process(name='myFunc', target=myFunc, args=(3, output_list))
    process_with_name.start()

    process_with_default_name = multiprocessing.Process(target=myFunc, args=(1, output_list))
    process_with_default_name.start()

    # Join processes in the order they were started
    process_with_default_name.join()
    process_with_name.join()

    return output_list




#سناریو دوممممممممممممممممممم
# توی این سناریو اومدم برای هر دو تا تابع نام رو ارسال کردم



def myFunc(sleep_time, output_list):
    name = multiprocessing.current_process().name
    output_str = f"Starting  {name}"
    output_list.append({"process_output": output_str})
    time.sleep(3)
    output_str = f"Exiting  {name}"
    output_list.append({"process_output": output_str})

@router.post("/scenario2_2_2", response_model=List[Dict[str, str]])
def run_processes():
    manager = multiprocessing.Manager()
    output_list = manager.list()

    # Start processes in the desired order
    process_with_name = multiprocessing.Process(name='myFunc', target=myFunc, args=(3, output_list))
    process_with_name.start()

    process_with_default_name = multiprocessing.Process(name='nahidazadi',target=myFunc, args=(1, output_list))
    process_with_default_name.start()

    # Join processes in the order they were started
    process_with_default_name.join()
    process_with_name.join()

    return output_list




#سناریو سومممممممممممممممممممممم

#اومدم ترتیب خروجی رو تغیر دادم یعنی هر کدوم استارت میشن و جوین میشن همچنین اومدم یک شی دیگر هم اضافه کردم که پارامتر نام را نمی گیرد از ورودی


def myFunc(sleep_time, output_list):
    name = multiprocessing.current_process().name
    output_str = f"Starting  {name}"
    output_list.append({"process_output": output_str})
    time.sleep(3)
    output_str = f"Exiting  {name}"
    output_list.append({"process_output": output_str})

@router.post("/scenario2_2_3", response_model=List[Dict[str, str]])
def run_processes():
    manager = multiprocessing.Manager()
    output_list = manager.list()

    # Start processes in the desired order
    process_with_name = multiprocessing.Process(name='myFunc', target=myFunc, args=(3, output_list))
    process_with_name.start()
    process_with_name.join()

    process_with_default_name = multiprocessing.Process(name='nahidazadi',target=myFunc, args=(1, output_list))
    process_with_default_name.start()
    process_with_default_name.join()

    process = multiprocessing.Process( target=myFunc, args=(1, output_list))
    process.start()
    process.join()

    return output_list








