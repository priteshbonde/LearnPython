import threading
import time

#$ 1: Extend Thread
class MyThread(threading.Thread):
    """
    This is how you add documentation to any thing
    """
    def __init__(self, name) :
        threading.Thread.__init__(self)
        self.name = name
        time.sleep(1)

    my_lock = threading.Lock()
    cooler = 1

    #$ 2: this is the entry point compulsory to add
    def run(self):
        
        for count in range(1,100):
            MyThread.my_lock.acquire()
            print(f"{self.name} {count} in run\n")
            MyThread.my_lock.release()
            time.sleep(1)

t1 = MyThread("Dhaaga")
t2 = MyThread("cord")
t1. start()
t2.start()


print("Main thread ends\n")