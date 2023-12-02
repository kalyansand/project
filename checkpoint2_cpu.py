from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.append(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

def print_file_lines(file_name="dram.txt"):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line, end='')

    except FileNotFoundError:
        print(f"Error: {file_name} not found.")

if __name__ == "__main__":
    pq = Queue()

    # Taking user input for CPU cycles
    cpu_cycle = int(input("Enter CPU cycle to check: "))

    pq.enqueue({
        'CPU CLOCK CYCLE': 100,
        'CHANNEL': 0,
        'DRAM COMMAND': 'PRE',
        'BANK GROUP': 0,
        'BANK': 0,
    })
    pq.enqueue({
        'CPU CLOCK CYCLE': 200,
        'CHANNEL': 0,
        'DRAM COMMAND': 'ACT0',
        'BANK GROUP': 0,
        'BANK': 0,
        'ROW': '03FF'
    })
    pq.enqueue({
        'CPU CLOCK CYCLE': 204,
        'CHANNEL': 0,
        'DRAM COMMAND': 'ACT1',
        'BANK GROUP': 0,
        'BANK': 0,
        'ROW': '03FF'
    })
    pq.enqueue({
        'CPU CLOCK CYCLE': 300,
        'CHANNEL': 0,
        'DRAM COMMAND': 'RD0',
        'BANK GROUP': 0,
        'BANK': 0,
        'COLUMN': 'EF'
    })
    pq.enqueue({
        'CPU CLOCK CYCLE': 304,
        'CHANNEL': 0,
        'DRAM COMMAND': 'RD1',
        'BANK GROUP': 0,
        'BANK': 0,
        'COLUMN': 'EF'
    })

    found = False

    # Checking if the CPU cycle matches any element in the queue
    for element in pq:
        if element['CPU CLOCK CYCLE'] == cpu_cycle:
            found = True
            print("Element matching CPU cycle found in the queue:")
            print(element)

            # Dequeue the element if possible
            if not pq.is_empty():
                dequeued_element = pq.dequeue()
                print("Dequeu Element:")
                print(dequeued_element)
            else:
                print("Queue is empty")

    if not found:
        print(f"No element found for CPU cycle {cpu_cycle} in the queue.")

    print(f'\nSize of the queue is: {pq.size()}')