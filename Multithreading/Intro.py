# sabse phle : concurrency kya hoti h 
#  concurrency: multiple tasks ko ek hi period me manage/progress karna
# concurrency ka mtlb necessarily ye nahi ki tasks exactly same time execute ho rhe hain
#  Mere pass 3 kaam h :-
# Task A:- File download karna , Task B:- Database Query, Task C:- API Request
# Normal sequential Program
#  A -------->
        #    B -------->
                    #  C -------->
# phle A complete, phir B, phir C
# CPU ek tasks se doosre task par switch kar skta h 

# Real World Scenario 
# m ek restaurant me hu 
# Customer A: order lia -> kitchen ko dia -> 
# Customer B: order lia 
# Customer C: order lia 
# Customer A ka food ready -> serve
# Customer B ka food ready -> serve
# waiter har customer ka food khud nhi bna rha 
# woh multiple tasks ko manage kar rha hai
# ye concurrency ka idea hai

# Parallelism kya hota h 
# it means multiple task literally simultaneously execute ho rhe h 
# suppose tumhre CPU me 4 cores hain
# Core 1: Task A
# Core 2: Task B
# Core 3: Task C
# Core 4: Task D
# ye actual parallel executoin hai

# Diffrence 
# Concurrency: A-> B-> A -> C -> B -> A
# Tasks ka progress interleaved ho skta h 

# Parallelism: 
# Core 1 -> AAAAAA
# Core 2 -> BBBBBB
# Core 3 -> CCCCCC
# Task same time par execute ho rhe h 

# Concurrency is about dealing with multiple tasks
# Parallelism is about executing multiple tasks simultaneously


# Threads kya hote h 
# import threading 
# thread ek execution path hai jo process ke andar run karta h 
# ek process ka andar multiple threads ho skte h 

# Process
# │
# ├── Thread 1
# ├── Thread 2
# ├── Thread 3
# └── Thread 4

# import threading

# def task():
#     print("Task running")

# t1 = threading.Thread(target=task)
# t2 = threading.Thread(target=task)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# Main Thread
#     │
#     ├── Thread 1
#     └── Thread 2

# Thread ka fyda kya hai 
# Threads especially useful hain jab program ka kaam :-
# network requests
# API calls
# file I/O
# database operations
# waiting
# downloading
# uploading
# download_file()
# agar download me 5s lag rhe h, cpu mostly wait kr rha h 

# Thread 1 → Download A
# Thread 2 → Download B
# Thread 3 → Download C
# Jab Thread 1 network ka response wait kar raha hai, doosra thread progress kar sakta hai.

# GIL:- Global Interpreter Lock
# CPython me GIL ek lock hai jo histrolically ensure karta h ek process ke andar ek waqt me sirf ek thread python bytecode execute kare
# means GIL bolta h ki ek process ke andar ek time pr ek thread python bytecode execute kare
# CPU
#  │
#  ├── Thread 1 ── 🔒 GIL
#  ├── Thread 2
#  └── Thread 3
# Thread 1 Python bytecode execute kar raha hai.
# Thread 2 ko Python bytecode execute karne ke liye GIL acquire karna padega.

# GIL kyu exist krta h 
# python ka memory management espically CPython ka refrence-counting based memory management thread safety ko simpler bnane ke lie GIL historically important rah h
# x = object
# internally Python objects ki lifetime/refrence counts manage hote hain
# multiple threads agar simultaenously interpreter-level object state modify karein, to synchronizstion problems ho skti h 
# GIL interpreter-level execution ko serialize karta h 

# Sabse important: GIL Point 
# Sab bolte h python threads ek saath nahi chal sakte
# ye oversimplification hai

# CPU bound python code:- 
# def calculate():
#     for i in range(100000000):
#         pass
# multiple threads generally multiple CPU cores par python bytecode ko true parallesim se execute nahi kar paate in tradional GIL enabled CPython
# Python threads CPU-bound work ke liye generally ideal nahi hote.

# 8. I/O-bound work me threads useful kyun hain?

# def download():
#     response = request.get(url)
# threads request bhejta hai
# Network
#    ↓
# WAITING...

# is waiting period me interpreter thread ko run kar sakte hai

# Thread 1 → API request → WAIT
#                          ↓
# Thread 2 → API request → WAIT
#                          ↓
# Thread 3 → process data
# Isliye threads I/O-bound applications me useful hain.

# Concurrency + Threads
# Threads concurrency implement karne ka ek method hain.

# import threading
# import time

# def task(name):
#     for i in range(3):
#         print(name, i)
#         time.sleep(1)

# t1 = threading.Thread(target=task, args=("A",))
# t2 = threading.Thread(target=task, args=("B",))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# Start and join kya karte h
# start(): thread ko actually start karta h 
# join(): main thread ko wait karne ko bolta h 
# Thread1 complete hone tak aage mat badho
# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("All tasks completed")

# Ab ek dangerous problem: Shared Data 
# counter = 0
#  Thread 1: counter += 1
# Thread 2: counter +=2
# expect krunga = 2
# but shared data me race condition ki vja se kuch bhi aa skta h 

# Race condition means 2 or more things ek hi chiz p kaam kre kio phle execute ho jye kio bdd m ho
# counter = 0

# Thread 1:
# read counter → 0

# Thread 2:
# read counter → 0

# Thread 1:
# write 1

# Thread 2:
# write 1

# iska solution h lock
# threading.lock()
# means ek time par ek thread ko critical section access karne do
# lock = threading.lock()

# lock.acquire()
# counter +=1
# lock.release()

# Thread 1 → acquire 🔒 → counter += 1 → release
                                    #   ↓
# Thread 2 → acquire 🔒 → counter += 1 → release

# better way
# with lock

# with lock:
    # counter +=1
# python automatically lock release kar deta h 

# import threading

# counter = 0
# lock = threading.Lock()

# def increment():
#     global counter

#     for _ in range(100000):
#         with lock:
#             counter += 1

# threads = []

# for _ in range(4):
#     t = threading.Thread(target=increment)
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# print(counter)