from queue import Queue
from collections import deque


class Queue:
        def __init__(self):
            self.buffer = []
    
        def enqueue(self, val):
            self.buffer.append(val)
            
        def dequeue(self):
            return self.buffer.pop()
        
        def is_empty(self):
            return len(self.buffer)==0
        
        def size(self):
            return len(self.buffer)
        def put(self, val):
            self.enqueue(val)

        def get(self):
            return self.dequeue()
        
memory_queue = Queue()
def address_mapping(memory_request_address):
    # Perform address mapping logic similar to the previous function
        # Convert the memory request address from hexadecimal to binary
    binary_address = bin(int(memory_request_address, 16))[2:].zfill(34)
    byte_select = int(binary_address[-1:], 2)
    low_column = int(binary_address[-5:-2], 2)
    channel = int(binary_address[-6], 2)
    bank_group = int(binary_address[-10:-7], 2)
    bank = int(binary_address[-13:-11], 2)
    column = int(binary_address[-19:-14], 2)
    row = int(binary_address[-36:-20], 2)

    # Print the extracted address components
    print(f' binary address of memory request : {memory_request_address}')
    print(f'{binary_address}')
    print(f"byte_select: {byte_select}")
    print(f"low_column: {low_column}")
    print(f"Channel: {channel}")
    print(f"Bank_group: {bank_group}")
    print(f"Bank: {bank}")
    print(f"Column: {column}")
    print(f"Row: {row}")

    return (byte_select,low_column,channel,bank_group,bank,column,row)
        #return (byte_select,low_column,channel,bank_group,bank,column,row)
def process_memory_requests(file_name="trace.txt", dram_file = "dram.txt"):
    # Initialize a queue to store memory request details

    

    # Read memory requests from the file
    with open(file_name, 'r') as file:
        for line in file:
            print(line, end='')
            
      
            # Extract memory request details
            cpu_cycle_time, core, operation, address = line.strip().split()

            # Perform address mapping for each memory request address
            mapping_details = address_mapping(address)


            # Encapsulate details into a dictionary
            request_details = {
                "cpu_cycle_time": int(cpu_cycle_time),
                "core": int(core),
                "operation": int(operation),
        
            
                "address": {
                    
                    "bank_group": mapping_details[0],
                    "bank": mapping_details[1],
            }
            }
            #print(request_details)
                # Push request details to the queue
            memory_queue.put({"controller":request_details})

        with open(dram_file, 'r') as dram_file:
            for line in dram_file:
            # Assuming the format of the DRAM commands in dram.txt is consistent with your requirements
                     # Extract memory request details
                        values = line.strip().split()
                        #print(values)
                        if len(values) >=3:
                            cycle_time, channel, dram_cmd  = values[:3]
                            details = {
                                "cycle_time":int(cycle_time),
                                "channel":int(channel),
                                "dram_cmd":str(dram_cmd),
                                # "bank_group":int(bank_group),
                                # "bank":int(bank),
                                # "row":str(row),
                                # "column":str(row),

                        }
                        print(details)
                        memory_queue.enqueue({"DIMM_cycle": details})
          #  else:
             #    print(f"Skipping line: {values}")

            return memory_queue

# # Process memory requests from the default file
# process_memory_requests()
result_queue = process_memory_requests()


# while not result_queue.empty():
#     print(result_queue.get())
print("Size of the queue:", memory_queue.size())
#while not memory_queue.is_empty():
print(memory_queue.dequeue())
#print(memory_queue.get())
# print(memory_queue.get())
# print(memory_queue.get())
# print(memory_queue.get())
# print(memory_queue.get())
# print(memory_queue.get())
# print(memory_queue.get())
# print(memory_queue.get())
# print(memory_queue.get())
# print(memory_queue.get())
print("Size of the queue:", memory_queue.size())