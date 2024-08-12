from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
import threading
import time




router = APIRouter()


#برای این کد باید ورودی بدی بهش اینیه که پایین نوشتم

#{
#   "items": 16
#}

class Box:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

box = Box()

class OperationRequest(BaseModel):
    items: int

@router.post("/scenario5_1")
def start_operations(request: OperationRequest):
    results = []
    lock = threading.Lock()  # Lock to coordinate the threads
    remove_started = False  # Flag to indicate if removing should start

    def adder():
        nonlocal results, remove_started
        items = request.items
        results.append(f"N° {items} items to ADD")
        while items > 0:
            box.add()
            time.sleep(1)
            items -= 1
            results.append(f"ADDED one item -->{items} item(s) to ADD")
            with lock:
                # Check if removing should start
                if not remove_started and box.total_items > 0:
                    remove_started = True

    def remover():
        nonlocal results, remove_started
        items = 1
        results.append(f"N° {items} items to REMOVE")
        while items > 0:
            with lock:
                if remove_started and box.total_items > 0:
                    box.remove()
                    items -= 1
                    results.append(f"REMOVED one item -->{items} item(s) to REMOVE")
            time.sleep(1)

    adder_thread = threading.Thread(target=adder)
    remover_thread = threading.Thread(target=remover)

    adder_thread.start()
    remover_thread.start()

    adder_thread.join()
    remover_thread.join()

    return {"status": "success", "results": results}

@router.get("/status")
def get_status():
    return {"total_items": box.total_items}








#اول می یاد همه رو اضافه میکنه بعد حذف میکنه همه رو

class Box:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)


box = Box()


class OperationRequest(BaseModel):
    items: int


@router.post("/scenario5_2")
def start_operations(request: OperationRequest):
    results = []
    items_to_add = request.items

    def add_items():
        for i in range(items_to_add, 0, -1):
            box.add()
            results.append(f"ADDED one item -->{i - 1} item(s) to ADD")
            time.sleep(1)  # Simulate some processing time

    def remove_items():
        for i in range(items_to_add):
            box.remove()
            results.append(f"REMOVED one item -->{items_to_add - i - 1} item(s) to REMOVE")
            time.sleep(1)  # Simulate some processing time

    # Add initial message
    results.append(f"N° {items_to_add} items to ADD")

    # Start adding items
    adder_thread = threading.Thread(target=add_items)
    adder_thread.start()
    adder_thread.join()  # Wait for adding to complete

    # Add removal message and start removing items
    results.append(f"N° {items_to_add} items to REMOVE")
    remover_thread = threading.Thread(target=remove_items)
    remover_thread.start()
    remover_thread.join()  # Wait for removing to complete

    return {"status": "success", "results": results}


@router.get("/status")
def get_status():
    return {"total_items": box.total_items}






# یه دونه اضافه میکنه یه دونه حذف می کنه برای همه باید اون ورودی رو قرار دهی

class Box:
    def __init__(self):
        self.lock = threading.RLock()
        self.total_items = 0

    def execute(self, value):
        with self.lock:
            self.total_items += value

    def add(self):
        with self.lock:
            self.execute(1)

    def remove(self):
        with self.lock:
            self.execute(-1)

box = Box()

class OperationRequest(BaseModel):
    items: int

@router.post("/scenario5_3")
def start_operations(request: OperationRequest):
    results = []
    lock = threading.Lock()  # Lock to coordinate the threads

    def adder_remover():
        nonlocal results
        items_to_add = request.items
        results.append(f"N° {items_to_add} items to ADD and REMOVE")

        while items_to_add > 0:
            with lock:
                # Add item
                box.add()
                items_to_add -= 1
                results.append(f"ADDED one item -->{items_to_add} item(s) to ADD")
                # Ensure removal if items_to_add is greater than zero
                if items_to_add >= 0:
                    time.sleep(1)  # Simulate time taken to process
                    box.remove()
                    results.append(f"REMOVED one item -->{items_to_add} item(s) to REMOVE")
            time.sleep(1)  # Simulate time taken between operations

    # Start adder/remover thread
    adder_remover_thread = threading.Thread(target=adder_remover)
    adder_remover_thread.start()
    adder_remover_thread.join()

    return {"status": "success", "results": results}

@router.get("/status")
def get_status():
    return {"total_items": box.total_items}

