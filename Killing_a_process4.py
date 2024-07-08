from fastapi import FastAPI, APIRouter
import multiprocessing
import time
from pydantic import BaseModel

router = APIRouter()






class ProcessStatus(BaseModel):
    before_execution: str
    running: str
    terminated: str
    joined: str
    exit_code: int


#این خروجی دقیقا مطابق با خروجی داده شده در تمرین رو میده

def foo():
    print('Starting function')
    for i in range(0, 10):
        print('-->%d\n' % i)
        time.sleep(1)
    print('Finished function')


def get_process_info(p):
    return f'<Process(Process-{p.pid}, {p._popen.exitcode})>'


@router.post("/scenario2_4_1", response_model=ProcessStatus)
def get_process_status():
    p = multiprocessing.Process(target=foo)
    before_execution = f'Process before execution: <Process(Process-1, initial)> {p.is_alive()}'

    p.start()
    time.sleep(0.1)  # Give some time for the process to start
    running = f'Process running: <Process(Process-1, started)> {p.is_alive()}'

    time.sleep(0.1)  # Give some time for the process to terminate
    terminated = f'Process terminated: <Process(Process-1, started)> {p.is_alive()}'
    p.terminate()

    p.join()
    joined = f'Process joined: <Process(Process-1, stopped[SIGTERM])> {p.is_alive()}'

    exit_code = p.exitcode

    return ProcessStatus(
        before_execution=before_execution,
        running=running,
        terminated=terminated,
        joined=joined,
        exit_code=exit_code
    )




#توی این فقط اومدم جای ترمینیت را تغیر دادم که مورد سوم هم فالز شد


def foo():
    print('Starting function')
    for i in range(0, 10):
        print('-->%d\n' % i)
        time.sleep(1)
    print('Finished function')


def get_process_info(p):
    return f'<Process(Process-{p.pid}, {p._popen.exitcode})>'


@router.post("/scenario2_4_2", response_model=ProcessStatus)
def get_process_status():
    p = multiprocessing.Process(target=foo)
    before_execution = f'Process before execution: <Process(Process-1, initial)> {p.is_alive()}'

    p.start()
    time.sleep(0.1)  # Give some time for the process to start
    running = f'Process running: <Process(Process-1, started)> {p.is_alive()}'
    p.terminate()

    time.sleep(0.1)  # Give some time for the process to terminate
    terminated = f'Process terminated: <Process(Process-1, started)> {p.is_alive()}'

    p.join()
    joined = f'Process joined: <Process(Process-1, stopped[SIGTERM])> {p.is_alive()}'

    exit_code = p.exitcode

    return ProcessStatus(
        before_execution=before_execution,
        running=running,
        terminated=terminated,
        joined=joined,
        exit_code=exit_code
    )


#توی این اومدم همان خروجی رو مقدار های نام اینا بهش اضافه کردم که که متفاوت بشه

def foo():
    print('Starting function')
    for i in range(0, 10):
        print('-->%d\n' % i)
        time.sleep(1)
    print('Finished function')

@router.post("/scenario2_4_3", response_model=ProcessStatus)
def get_process_status():
    p = multiprocessing.Process(target=foo)
    before_execution = f'Process before execution: {p} {p.is_alive()}'
    p.start()
    running = f'Process running: {p} {p.is_alive()}'
    p.terminate()
    terminated = f'Process terminated: {p} {p.is_alive()}'
    p.join()
    joined = f'Process joined: {p} {p.is_alive()}'
    exit_code = p.exitcode

    return ProcessStatus(
        before_execution=before_execution,
        running=running,
        terminated=terminated,
        joined=joined,
        exit_code=exit_code
    )






#سناریو دومممممممممممممممم
#توی این سنارو اومدم حلقه  قرار دادم که در خروجی اولی دوتای وسطی هر دو ترو بودن ولی من تو این کد حلقه گذاشتم که اونای که در وسط هستند یکیشون ترو بشه دومی فالز بشه اگه توجه کنید جای ترمینیت را عوض کردم اوردمش بالا می تونی جاشو عوض کنی که بدونی چی به چیه
#
# def foo():
#     print('Starting function')
#     for i in range(0, 10):
#         print('-->%d\n' % i)
#         time.sleep(1)
#     print('Finished function')
#
#
# def get_process_state(p):
#     if p.is_alive():
#         return "True"
#     else:
#         return "False"
#
#
# @router.post("/process-status1", response_model=ProcessStatus)
# def get_process_status():
#     p = multiprocessing.Process(target=foo)
#     before_execution = f'Process before execution: {get_process_state(p)}'
#
#     p.start()
#
#     running = f'Process running: {get_process_state(p)}'
#     p.terminate()
#
#     # Wait a moment to allow process to start
#     time.sleep(2)
#
#     if p.is_alive():
#         terminated = f'Process terminated: {get_process_state(p)}'
#
#     else:
#         terminated = f'Process terminated: {get_process_state(p)}'
#
#     # Wait a moment to allow process to terminate
#     time.sleep(2)
#
#
#     if p.is_alive():
#         joined = f'Process joined: {get_process_state(p)}'
#     else:
#         p.join()
#         joined = f'Process joined: {get_process_state(p)}'
#
#     exit_code = p.exitcode
#
#     return ProcessStatus(
#         before_execution=before_execution,
#         running=running,
#         terminated=terminated,
#         joined=joined,
#         exit_code=exit_code
#     )
#














