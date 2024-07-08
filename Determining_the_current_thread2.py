from typing import List
import uvicorn
from fastapi import FastAPI, HTTPException, Request, BackgroundTasks,APIRouter
from pydantic import BaseModel
import threading
import time

router=APIRouter()


# Global lists to hold the status of each function
output_A = []
output_B = []
output_C = []

def function_A():
    global output_B
    #output_A = []
    output_A.append(threading.current_thread().name + '--> starting')
    time.sleep(2)
    output_A.append(threading.current_thread().name + '--> exiting')

def function_B():
    global output_B
    #output_B = []
    output_B.append(threading.current_thread().name + '--> starting')
    time.sleep(2)
    output_B.append(threading.current_thread().name + '--> exiting')

def function_C():
    global output_C
    #output_C= []
    output_C.append(threading.current_thread().name + '--> starting')
    time.sleep(2)
    output_C.append(threading.current_thread().name + '--> exiting')

@router.post("/scenario2_1")
def run_functions():
    global output_A, output_B, output_C
    # Reset outputs

    # Create threads for each function
    t1 = threading.Thread(name='function_A', target=function_A)
    t2 = threading.Thread(name='function_B', target=function_B)
    t3 = threading.Thread(name='function_C', target=function_C)

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    # Join threads to ensure they complete
    t1.join()
    t2.join()
    t3.join()

    # Return the output of each function
    return {
        1: output_A[0],
        2: output_B[0],
        3: output_C[0],
        4: output_A[1],
        5: output_B[1],
        6: output_C[1]
    }



@router.post("/scenario2_2")
def run_functions1():
    global output_A, output_B, output_C
    # Reset outputs
    output_A, output_B, output_C = [], [], []

    # Create threads for each function
    t1 = threading.Thread(name='function_A', target=function_A)
    t2 = threading.Thread(name='function_B', target=function_B)
    t3 = threading.Thread(name='function_C', target=function_C)

    # Start threads one after the other
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()

    # Return the output of each function

    return {
        1: output_A[0],
        2: output_A[1],
        3: output_B[0],
        4: output_B[1],
        5: output_C[0],
        6: output_C[1]
    }


@router.post("/scenario2_3")
def run_functions2():
    global output_A, output_B, output_C
    # Reset outputs
    #output_A, output_B, output_C = [], [], []

    # Create threads for each function
    t1 = threading.Thread(name='function_A', target=function_A)
    t2 = threading.Thread(name='function_B', target=function_B)
    t3 = threading.Thread(name='function_C', target=function_C)

    # Start threads without waiting for each to finish before starting the next
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    t3.start()
    t3.join()

    # Wait for all threads to complete


    # Return the output of each function
    return {
        1: output_A[0],
        2: output_B[0],
        3: output_A[1],
        4: output_B[1],
        5: output_C[0],
        6: output_C[1]
    }
