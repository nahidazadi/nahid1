from fastapi import FastAPI, APIRouter
import multiprocessing
import time
from pydantic import BaseModel
import multiprocessing
from pydantic import BaseModel

router = APIRouter()



class ProcessStatus(BaseModel):
    message: str



# خروجی که ازمون خواسته شده را نمایش میده

class MyProcess(multiprocessing.Process):
    def run(self):
        print(f'called run method by {self.name}')
        return


@router.post("/scenario2_5_1/", response_model=list[ProcessStatus])
def start_processes():
    messages = []
    for i in range(1, 11):
        process = MyProcess()
        process.name = f'Process-{i}'
        process.start()
        process.join()  # This ensures the process completes before starting the next one
        messages.append(ProcessStatus(message=f'called run method by {process.name}'))

    return messages









# این کد می اید معکوس میکند خروجی رو از بزرگ به کوچیک نمایش میده

class MyProcess(multiprocessing.Process):
    def run(self):
        print(f'called run method by {self.name}')
        return

@router.post("/scenario2_5_2/", response_model=list[ProcessStatus])
def start_processes():
    messages = []
    for i in range(1, 11):
        process = MyProcess()
        process.name = f'Process-{i}'
        process.start()
        process.join()  # This ensures the process completes before starting the next one
        messages.append(ProcessStatus(message=f'called run method by {process.name}'))

    messages.reverse()  # Reverse the list to print messages from largest to smallest
    return messages





# این کد میاد اول زوج هارو نمایش میده بعد فرد هارو

class MyProcess(multiprocessing.Process):
    def run(self):
        print(f'called run method by {self.name}')
        return


@router.post("/scenario2_5_3/", response_model=list[ProcessStatus])
def start_processes():
    even_messages = []
    odd_messages = []

    for i in range(1, 11):
        process = MyProcess()
        process.name = f'Process-{i}'
        process.start()
        process.join()  # This ensures the process completes before starting the next one
        message = ProcessStatus(message=f'called run method by {process.name}')

        if i % 2 == 0:
            even_messages.append(message)
        else:
            odd_messages.append(message)

    messages = even_messages + odd_messages  # Combine even and odd messages
    return messages






