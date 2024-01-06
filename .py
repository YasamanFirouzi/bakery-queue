import threading
import time
from queue import Queue

class Nanavayi:
    def __init__(self):
        self.queue1 = Queue()   # queue 1
        self.queue2 = Queue()   # queue 2

    def add_order(self, order):
        if self.queue1.qsize() <= 3:
            self.queue1.put(order)
        else:
            self.queue2.put(order)

    def process_orders(self):
        while True:
            if not self.queue1.empty(): #if queue1 is not empty, get order
                order = self.queue1.get()
                self._process_order(order)
            if not self.queue2.empty(): #if queue2 is not empty, get order
                order = self.queue2.get()   
                self._process_order(order)
            time.sleep(1)  # Delay to reject people

    def _process_order(self, order):
        customer, bread_type, cook_time = order
        print(f"Bakery: order {bread_type} for {customer} received.")
        print(f"Bakery: Baking bread for {customer}...")
        time.sleep(cook_time)  # Bread baking time
        print(f"Bakery: Bread for {customer} is ready.")

nanavayi = Nanavayi()

def main():
    nanavayi.add_order(("Customer 1", "sangak bread", 5))  # 5 for the baking time of the customer's bread
    nanavayi.add_order(("Customer 2", "Taftoun bread", 3))
    nanavayi.add_order(("Customer 3", "Taftoun bread", 3))
    nanavayi.add_order(("Customer 4", "Lavash Bread", 4))
    nanavayi.add_order(("Customer 5", "sangak bread", 5))
    nanavayi.process_orders()

# Start the main function in a separate thread
thread = threading.Thread(target=main)
thread.start()

# Wait for the thread to finish
thread.join()
