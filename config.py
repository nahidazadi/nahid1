from fastapi import FastAPI
import Defining_a_thread1
import Defining_a_thread_subclass3
import Defining_processes_in_a_subclass5
import Determining_the_current_thread2
import Killing_a_process4
import Naming_a_process2
import Running_processes_in_the_background3
import Spawning_a_process1
import Synchronizing_processes7
import Thread_synchronization_with_RLock5
import Thread_synchronization_with_a_barrier7
import Thread_synchronization_with_a_lock4
import Thread_synchronization_with_semaphores6
import Using_a_process_pool8
import acc

app=FastAPI()

app.include_router(Defining_a_thread1.router,tags=["Defining_a_thread1"])
app.include_router(Determining_the_current_thread2.router,tags=["Determining_the_current_thread2"])
app.include_router(Defining_a_thread_subclass3.router,tags=["Defining_a_thread_subclass3"])
app.include_router(Thread_synchronization_with_a_lock4.router,tags=["Thread_synchronization_with_a_lock4"])
app.include_router(acc.router,tags=["acc"])
app.include_router(Thread_synchronization_with_RLock5.router,tags=["Thread_synchronization_with_RLock5"])
app.include_router(Thread_synchronization_with_semaphores6.router,tags=["Thread_synchronization_with_semaphores6"])
app.include_router(Thread_synchronization_with_a_barrier7.router,tags=["Thread_synchronization_with_a_barrier7"])

#فایل های تمرینات دوم

app.include_router(Spawning_a_process1.router,tags=["Spawning_a_process1"])
app.include_router(Naming_a_process2.router,tags=["Naming_a_process2"])
app.include_router(Running_processes_in_the_background3.router,tags=["Running_processes_in_the_background3"])
app.include_router(Killing_a_process4.router,tags=["Killing_a_process4"])
app.include_router(Defining_processes_in_a_subclass5.router,tags=["Defining_processes_in_a_subclass5"])
app.include_router(Synchronizing_processes7.router,tags=["Synchronizing_processes7"])
app.include_router(Using_a_process_pool8.router,tags=["Using_a_process_pool8"])
