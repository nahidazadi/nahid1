from random import randrange
from fastapi import FastAPI, APIRouter, BackgroundTasks
from threading import Barrier, Thread
from time import ctime, sleep
from typing import List, Dict, Optional
from random import randrange


router = APIRouter()





num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']
results = []

def runner(name: str, delay: int):
    sleep(delay)
    finish_line.wait()  # همه دوندگان اینجا صبر می‌کنند
    result = {
        'name': name,
        'time': ctime()  # زمانی که دوندگان به مانع می رسن
    }
    print(f"{name} reached the barrier at: {result['time']}")
    results.append(result)

@router.post("/scenario7_1", response_model=List[Dict[str, str]])
def start_race(scenario: Optional[int] = 1):
    global runners, results, finish_line
    # Reset the global state for each race
    runners = ['Huey', 'Dewey', 'Louie']
    results = []
    finish_line = Barrier(num_runners)

    # Define delays based on scenario
    if scenario == 3:
        delays = [1, 2, 3]  # همه دوندگان یک تأخیر دارند
    else:
        delays = [randrange(2, 5) for _ in range(num_runners)]  # تأخیرهای تصادفی

    threads = []
    print('START RACE!!!!')
    for i in range(num_runners):
        name = runners.pop(0)
        threads.append(Thread(target=runner, args=(name, delays[i])))
        threads[-1].start()
    for thread in threads:
        thread.join()

    print('Race over!')
    return results








#نتایج بعد از مسابقه معکوس می شود runners


num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']
results = []

def runner(name: str, delay: int):
    sleep(delay)
    finish_line.wait()  # همه دوندگان اینجا صبر می‌کنند
    result = {
        'name': name,
        'time': ctime()  # همه در یک زمان گزارش می‌دهند
    }
    print(f"{name} reached the barrier at: {result['time']}")
    results.append(result)

@router.post("/scenario7_2", response_model=List[Dict[str, str]])
def start_race(scenario: Optional[int] = 1):
    global runners, results, finish_line
    # Reset the global state for each race
    runners = ['Huey', 'Dewey', 'Louie']
    results = []
    finish_line = Barrier(num_runners)

    # Define delays randomly
    delays = [randrange(2, 5) for _ in range(num_runners)]  # تأخیرهای تصادفی

    threads = []
    print('START RACE!!!!')
    # Reverse the list of runners

    for i in range(num_runners):
        name = runners.pop()
        threads.append(Thread(target=runner, args=(name, delays[i])))
        threads[-1].start()
    for thread in threads:
        thread.join()

    print('Race over!')


    return results[::-1]






#این شافل میکند دوندگان رو و به صورت رندم به خط پایان می رسند


num_runners = 3
finish_line = Barrier(num_runners)
runners = ['Huey', 'Dewey', 'Louie']
results = []

def runner(name: str, delay: int):
    sleep(delay)
    finish_line.wait()  # همه دوندگان اینجا صبر می‌کنند
    result = {
        'name': name,
        'time': ctime()  # همه در یک زمان گزارش می‌دهند
    }
    print(f"{name} reached the barrier at: {result['time']}")
    results.append(result)

@router.post("/scenario7_3", response_model=List[Dict[str, str]])
def start_race(scenario: Optional[int] = 1):
    global runners, results, finish_line
    # Reset the global state for each race
    runners = ['Huey', 'Dewey', 'Louie']
    results = []
    finish_line = Barrier(num_runners)

    # Define delays randomly
    delays = [randrange(2, 5) for _ in range(num_runners)]  # تأخیرهای تصادفی

    threads = []
    print('START RACE!!!!')
    # Shuffle runners randomly
    import random
    random.shuffle(runners)

    for i in range(num_runners):
        name = runners.pop()
        threads.append(Thread(target=runner, args=(name, delays[i])))
        threads[-1].start()
    for thread in threads:
        thread.join()

    print('Race over!')
    return results



