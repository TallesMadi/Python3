from time import sleep
from threading import Thread, Lock

class MyThread(Thread):
    def __init__(self, text: str, time: int | float) -> None:
        self.text = text
        self.time = time
        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)

class Tickets:
    def __init__(self, inventory: int) -> None:
        self.inventory = inventory
        self.lock = Lock()

    def buy(self, amount):
        self.lock.acquire()
        if self.inventory < amount:
            print('Não temos ingressos suficientes!')
        else:
            self.inventory -= amount
            print(f'Você comprou {amount} ingressos. Ainda temos {self.inventory}') 
        self.lock.release()

if __name__ == '__main__':
    ticket = Tickets(10)

    for i in range(11):
        t = Thread(target=ticket.buy, args=(i,))
        t.start()
