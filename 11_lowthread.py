import _thread
import time

cooler = 1
cooler_lock = _thread.allocate_lock() #! this is the lock

#$ This is main thread
def backGround(name):
    global cooler
    for count in range(1,10):
        time.sleep(1)
        cooler_lock.acquire()
        print(f" BG {name} {cooler} ")
        cooler+=1
        print(f"some more ops {(count * 10) + 14 }")
        cooler_lock.release()

#! background thread - Daemon thread (Detached) thread and are ignored on program end
t1 = _thread.start_new_thread(backGround, ("Turing",))
t2 = _thread.start_new_thread(backGround, ("Guido",))

for count in range(1,10):
    time.sleep(1)
    print(f" Main {count} ")


#$ Main Thread ends here
print("Ending the main thread")
