import time
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime
import multiprocessing
from multiprocessing import Barrier, Lock, Process, Queue
from time import time

router = APIRouter()




from fastapi import FastAPI, APIRouter, HTTPException
from datetime import datetime
import multiprocessing
from multiprocessing import Barrier, Lock, Process, Queue
from time import time, sleep


def test_with_barrier(synchronizer, serializer, result_queue):
    name = multiprocessing.current_process().name
    barrier_cross_time = time()  # Time when the process reaches and crosses the barrier
    synchronizer.wait()  # Wait for the barrier
    now = time()  # Time when the process finishes after crossing the barrier
    with serializer:
        result_queue.put({
            "process": name,
            "barrier_cross_time": datetime.fromtimestamp(barrier_cross_time).isoformat(),
            "finish_time": datetime.fromtimestamp(now).isoformat(),
            "has_barrier": True
        })

def test_without_barrier(result_queue):
    name = multiprocessing.current_process().name
    now = time()  # Time when the process finishes
    result_queue.put({
        "process": name,
        "barrier_cross_time": None,  # No barrier for this process
        "finish_time": datetime.fromtimestamp(now).isoformat(),
        "has_barrier": True
    })

@router.post("/scenario2_7_1")
def start_processes1():
    try:
        result_queue = Queue()

        # Define the synchronizer and serializer
        synchronizer = Barrier(2)
        serializer = Lock()

        # Start processes with and without barrier
        p1 = Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, result_queue))
        p2 = Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, result_queue))
        p3 = Process(name='p3 - test_without_barrier', target=test_without_barrier, args=(result_queue,))
        p4 = Process(name='p4 - test_without_barrier', target=test_without_barrier, args=(result_queue,))

        # Start all processes
        p1.start()
        p2.start()
        p3.start()
        p4.start()

        # Wait for all processes to finish
        p1.join()
        p2.join()
        p3.join()
        p4.join()

        # Collect results
        results = []
        while not result_queue.empty():
            results.append(result_queue.get())

        # Sort results based on barrier status and finish time
        sorted_results = sorted(results, key=lambda x: (x['has_barrier'], x['finish_time']))

        return {"message": "Processes completed", "results": sorted_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



#دوتای اخری از مانع استفاده می کنن

def test_without_barrier(result_queue):
    name = multiprocessing.current_process().name
    now = time()  # Time when the process finishes
    result_queue.put({
        "process": name,
        "barrier_cross_time": None,  # No barrier time for this process
        "finish_time": datetime.fromtimestamp(now).isoformat(),
        "has_barrier": False
    })

def test_with_barrier(synchronizer, serializer, result_queue):
    name = multiprocessing.current_process().name
    synchronizer.wait()  # Wait for the barrier
    barrier_cross_time = time()  # Time when the process reaches and crosses the barrier
    now = time()  # Time when the process finishes
    with serializer:
        result_queue.put({
            "process": name,
            "barrier_cross_time": datetime.fromtimestamp(barrier_cross_time).isoformat(),  # Barrier time for this process
            "finish_time": datetime.fromtimestamp(now).isoformat(),
            "has_barrier": True
        })

@router.post("/scenario2_7_2")
def start_processes1():
    try:
        result_queue = Queue()

        # Define the synchronizer and serializer
        synchronizer = Barrier(2)  # Adjust barrier to 2
        serializer = Lock()

        # Start processes with and without barrier
        p1 = Process(name='p1 - test_without_barrier', target=test_without_barrier, args=(result_queue,))
        p2 = Process(name='p2 - test_without_barrier', target=test_without_barrier, args=(result_queue,))
        p3 = Process(name='p3 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, result_queue))
        p4 = Process(name='p4 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, result_queue))

        # Start all processes
        p1.start()
        p2.start()
        p3.start()
        p4.start()

        # Wait for all processes to finish
        p1.join()
        p2.join()
        p3.join()
        p4.join()

        # Collect results
        results = []
        while not result_queue.empty():
            results.append(result_queue.get())

        # Sort results based on barrier status and finish time
        sorted_results = sorted(results, key=lambda x: (x['has_barrier'], x['finish_time']))

        return {"message": "Processes completed", "results": sorted_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





#اومدم یه فرایند دیگه اظافه کردم که از مانع اونم استفاده میکند سه فرایند از مانع استفاده می کنند

def test_with_barrier(synchronizer, serializer, result_queue):
    name = multiprocessing.current_process().name
    barrier_cross_time = time()  # Time when the process reaches and crosses the barrier
    synchronizer.wait()  # Wait for the barrier
    now = time()  # Time when the process finishes after crossing the barrier
    with serializer:
        result_queue.put({
            "process": name,
            "barrier_cross_time": datetime.fromtimestamp(barrier_cross_time).isoformat(),
            "finish_time": datetime.fromtimestamp(now).isoformat(),
            "has_barrier": True
        })

def test_without_barrier(result_queue):
    name = multiprocessing.current_process().name
    now = time()  # Time when the process finishes
    result_queue.put({
        "process": name,
        "barrier_cross_time": None,  # No barrier for this process
        "finish_time": datetime.fromtimestamp(now).isoformat(),
        "has_barrier": False
    })

@router.post("/scenario2_7_3")
def start_processes1():
    try:
        result_queue = Queue()

        # Define the synchronizer and serializer
        synchronizer = Barrier(3)
        serializer = Lock()

        # Start processes with and without barrier
        p1 = Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, result_queue))
        p2 = Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, result_queue))
        p3 = Process(name='p3 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, result_queue))

        p4 = Process(name='p4 - test_without_barrier', target=test_without_barrier, args=(result_queue,))
        p5 = Process(name='p5 - test_without_barrier', target=test_without_barrier, args=(result_queue,))

        # Start all processes
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()

        # Wait for all processes to finish
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()

        # Collect results
        results = []
        while not result_queue.empty():
            results.append(result_queue.get())

        # Sort results based on barrier status and finish time
        sorted_results = sorted(results, key=lambda x: (x['has_barrier'], x['finish_time']))

        return {"message": "Processes completed", "results": sorted_results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


















#توی این سناریو زمان ثبت شدن در صف را به ما میده
#
# from fastapi import FastAPI, APIRouter, HTTPException
# from datetime import datetime
# import multiprocessing
# from multiprocessing import Barrier, Lock, Process, Queue
# from time import time
#
#
#
# def test_with_barrier(synchronizer, serializer, result_queue):
#     name = multiprocessing.current_process().name
#     # Wait for the barrier and record the time of crossing the barrier
#     barrier_cross_time = time()
#     synchronizer.wait()  # Wait for the barrier
#     now = time()  # Record the time when the process finishes after crossing the barrier
#     with serializer:
#         result_queue.put({
#             "process": name,
#             "barrier_cross_time": datetime.fromtimestamp(barrier_cross_time).isoformat(),
#             "finish_time": datetime.fromtimestamp(now).isoformat(),
#             "has_barrier": True
#         })
#
# def test_without_barrier(result_queue):
#     name = multiprocessing.current_process().name
#     now = time()  # Record the time when the process finishes
#     result_queue.put({
#         "process": name,
#         "barrier_cross_time": None,  # No barrier for this process
#         "finish_time": datetime.fromtimestamp(now).isoformat(),
#         "has_barrier": False
#     })
#
# @router.post("/start_processes1")
# def start_processes1():
#     try:
#         result_queue = Queue()
#
#         # Define the synchronizer and serializer
#         synchronizer = Barrier(2)
#         serializer = Lock()
#
#         # Start processes with and without barrier
#         p1 = Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, result_queue))
#         p2 = Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer, result_queue))
#         p3 = Process(name='p3 - test_without_barrier', target=test_without_barrier, args=(result_queue,))
#         p4 = Process(name='p4 - test_without_barrier', target=test_without_barrier, args=(result_queue,))
#
#         # Start all processes
#         p1.start()
#         p2.start()
#         p3.start()
#         p4.start()
#
#         # Wait for all processes to finish
#         p1.join()
#         p2.join()
#         p3.join()
#         p4.join()
#
#         # Collect results
#         results = []
#         while not result_queue.empty():
#             results.append(result_queue.get())
#
#         # Sort results to ensure that processes without barriers are listed first
#         sorted_results = sorted(results, key=lambda x: (x['has_barrier'], x['barrier_cross_time'], x['finish_time']))
#
#         return {"message": "Processes completed", "results": sorted_results}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#
#
#
#





