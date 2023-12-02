from collections import deque
import sys


class Queue:
        def __init__(self):
            self.buffer = []
    
        def enqueue(self, val):
            self.buffer.append(val)
            
        def dequeue(self):
            return self.buffer.pop(0)
        
        def is_empty(self):
            return len(self.buffer)==0
        
        def size(self):
            return len(self.buffer)

pq = Queue()

pq.enqueue({
    'CPU CLOCK CYCLE' : 100,
    'CHANNEL' : 0,
    'DRAM COMMAND' : 'PRE',
    'BANK GROUP' : 0,
    'BANK' : 0,
})
pq.enqueue({
    'CPU CLOCK CYCLE' : 200,
    'CHANNEL' : 0,
    'DRAM COMMAND' : 'ACT0',
    'BANK GROUP' : 0,
    'BANK' : 0,
    'ROW' : '03FF'
})
pq.enqueue({
    'CPU CLOCK CYCLE' : 204,
    'CHANNEL' : 0,
    'DRAM COMMAND' : 'ACT1',
    'BANK GROUP' : 0,
    'BANK' : 0,
    'ROW' : '03FF'
})
pq.enqueue({
    'CPU CLOCK CYCLE' : 300,
    'CHANNEL' : 0,
    'DRAM COMMAND' : 'RD0',
    'BANK GROUP' : 0,
    'BANK' : 0,
    'COLUMN' : 'EF'
})
pq.enqueue({
    'CPU CLOCK CYCLE' : 304,
    'CHANNEL' : 0,
    'DRAM COMMAND' : 'RD1',
    'BANK GROUP' : 0,
    'BANK' : 0,
    'COLUMN' : 'EF'
})

def print_file_lines(file_name="C:\\Users\\sripa\\OneDrive\\Desktop\\MSD_PROJECT\\project\\dram.txt"):
    try:
        file = open(file_name, 'r')
        line = file.read()
        print(line, end='')
        
        
    except FileNotFoundError:
        print(f"Error: {file_name}  not found.")
# print("Enable the IF main function below to print the data in dram.txt")
# if __name__ == "__main__":
    
    if len(sys.argv)-1 == 0:
        
       print_file_lines()
    else:
        file_name = sys.argv[1]
        new_file = open(file_name, 'w')
        new_stdout = sys.stdout
        sys.stdout = new_file
        print_file_lines()
        sys.stdout = new_stdout
        new_file = open(file_name, 'r')
        line = new_file.read()
        print(line, end='')   
        
        
         


# print("Remove '#' for below print statements for stubs to remove the items in queue sequentially")
print(f' \n{pq.dequeue()}')
# print(f' \n{pq.dequeue()}')
# print(f' \n{pq.dequeue()}')
# print(f' \n{pq.dequeue()}')
# print(f' \n{pq.dequeue()}')
print(f'\n\nSize of the queue is :{pq.size()}')


