from time import sleep
from threading import Thread

class MyThread(Thread):
    def __init__(self, text: str, time: int | float) -> None:
        self.text = text
        self.time = time
        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)
    
thread1 = MyThread('Thread 1', 5)
thread1.start()

thread2 = MyThread('Thread 2', 7)
thread2.start()

thread3 = MyThread('Thread 3', 1)
thread3.start()

def it_will_take_time(time, text):
    sleep(time)
    print(text)

t = Thread(target=it_will_take_time, args=(10, 'Thread Function'))
t.start()

# while t.is_alive():
#     print('...')
#     sleep(1)

for i in range(20):
    print(i)
    sleep(1)
