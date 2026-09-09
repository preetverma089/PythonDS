#  Concurrency and parallism 
#  Concurrrency means doing multiple tasks at diffrent time
# Parellism :  execute multiple tasks at single time
# Parallism: ye diffrent tasks k lie diffrent cpu core use krta h 

# Parallelism me agar 6 cpu cores lge hue h agar kio bhi cpu core slow h to jb tk srre apna kaam complete ni kr lete 
# tb tk execution result ni milega kisi ka bhi
# but concurrnecty me kya hota h ek cpu core srre kaam kr deta h jse kaam pura hota h vse hi result mil jta h vo 
# rely nhi krta iss chiz p ki srre execution ho tb result mile


# Concurrency                                             Parallelism
# threading.Thread                                        Multiprocessing.Process
# asyncio                                                 Concurrent,futures.ProcessPoolExecutor

# Examples of Concurrency:- 

# MultiThreading 

# import threading
# import time

# def take_orders():
#     for i in range(1,4):
#         print(f"Taking order for {i}")
#         time.sleep(1)

# def brew_chai():
#     for i in range(1,4):
#         print(f"Brewing the chai for {i}")
#         time.sleep(5)

# # how to create the threads
# order_thread = threading.Thread(target = take_orders)
# brew_Thread = threading.Thread(target = brew_chai)

# order_thread.start()
# brew_Thread.start()

# # wait for both to finish
# order_thread.join()
# brew_Thread.join()

# print(f"All orders taken and chai brewed")

# MultiProcessing 

from multiprocessing import Process
import time

def brew_Chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"End of {name} chai brewing")

if __name__ == "__main__":

    chai_makers = [
        Process(
            target=brew_Chai,
            args=(f"Chai Maker #{i+1}",)
        )
        for i in range(3)
    ]

    # Start all Process
    for p in chai_makers:
        p.start()

    # Wait for all complete
    for p in chai_makers:
        p.join()

    print("all chai served")