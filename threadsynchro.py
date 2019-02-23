from threading import Thread,Lock,current_thread
from time import sleep
class Railway:
    def __init__(self,available):
        self.available=available
        self.lock=Lock()
    def reserve(self,wanted):
        self.lock.acquire()
        if self.available>=wanted:
            name=current_thread().getName()
            print('{}seats alloated to {}'.format(wanted,name))
            sleep(4)
            self.available-=wanted
        else:
            print("sorry seats are not available for: ",current_thread().getName())
            self.lock.release()
class First(Thread):
    def run(self):
        r.reserve(2)
class Second(Thread):
    def run(self):
        r.reserve(2)
#calling block
r=Railway(1)
f=First()
s=Second()
f.setName('user1')
s.setName('user2')
f.start()
s.start()

