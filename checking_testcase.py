# Address mapping function (unchanged)
import sys
def address_mapping(memory_request_addresses):
    with open("address_map.txt", 'w') as file:
        for memory_request_address in memory_request_addresses:
            binary_address = bin(int(memory_request_address, 16))[2:].zfill(34)
            low_column = hex(int(binary_address[-6:-2], 2))[2:]
            bank_group = int(binary_address[-10:-7], 2)
            bank = int(binary_address[-12:-10], 2)
            row = hex(int(binary_address[-18:-12], 2))
            column = hex(int(binary_address[:-18], 2))

            print(f' binary address of memory request: {memory_request_address}', file=file)
            print(f'{binary_address}', file=file)
            print(f"Below is address mapping info", file=file)
            print(f"low_column: {low_column}", file=file)
            print(f"Bank_group: {bank_group}", file=file)
            print(f"Bank: {bank}", file=file)
            print(f"Column: {column}", file=file)
            print(f"Row: {row}", file=file)
            print("\n", file=file)

    return "Address mapping information has been written to 'address_map.txt'."
    
# Function to read and parse input file (unchanged)
def read_input_trace(file_name):
    memory_requests = []
    with open(file_name, 'r') as file:
        for line in file:
            time, core, operation, address = line.strip().split()
            memory_requests.append({
                "time": int(time),
                "core": int(core),
                "operation": int(operation),
                "address": address
            
                

                
            })
         
                 
    return memory_requests

# Generate DRAM commands based on memory operation type
def generate_dram_commands(memory_requests):
    dram_commands = []
    dim_time = 2
    channel = 0

    for request in memory_requests:
        time = request["time"]
        operation = request["operation"]
        address = request["address"]
        
        low_column,bank_group, bank, row, column = address_mapping(address)
        
        if operation == 0 or operation == 2:
            #print(read_input_trace())
            # print(f"At every cpu cycle time: {time}")
            dram_commands.append(f"At this cpu time{time} ns")
            dram_commands.append(f"{dim_time} {channel} ACT0 {bank_group} {bank} {row}")
           # dim_time += 2
            dram_commands.append(f"{dim_time} {channel} ACT1 {bank_group} {bank} {row}")
           # dim_time += 2
            dram_commands.append(f"{dim_time} {channel} RD0  {bank_group} {bank} {column}{low_column}")
           # dim_time += 2
            dram_commands.append(f"{dim_time} {channel} RD1  {bank_group} {bank} {column}{low_column}")
            #dim_time += 2
            dram_commands.append(f"{dim_time} {channel} PRE  {bank_group} {bank}")
            dim_time += 2
        elif operation == 1:
           # print(f"At every cpu cycle time: {time}")
            # add_time = input(f"enter a cycle time:")
            # dim_time += int(add_time)
            dram_commands.append(f"At this cpu time{time} ns")
            dram_commands.append(f"{dim_time} {channel} ACT0 {bank_group} {bank} {row}")
            #print(dram_commands.append)
           # dim_time += 1
            dram_commands.append(f"{dim_time} {channel} ACT1 {bank_group} {bank} {row}")
           # dim_time += 2
            dram_commands.append(f"{dim_time} {channel} WR0  {bank_group} {bank} {column}{low_column}")
           # dim_time += 4
            dram_commands.append(f"{dim_time} {channel} WR1  {bank_group} {bank} {column}{low_column}")
           # dim_time += 4
            dram_commands.append(f"{dim_time} {channel} PRE  {bank_group} {bank}")
            dim_time += 2
    return dram_commands

# Input trace file
input_file = input ("Enter any test file ") or "trace.txt"  # Replace with your input file name

with open("dram.txt", "w") as file:
            file.write('')
# Read input trace file
input_requests = read_input_trace(input_file)

# Generate DRAM commands for all requests
dram_commands_list = generate_dram_commands(input_requests)

# Define a queue to hold the DRAM commands
dram_queue = []
wait = []

# Check if the queue is full
def is_queue_full(queue):
    return len(queue) >= 16

# Function to pop from queue and write to output file
def pop_from_queue(queue):
    if queue:
        command = queue.pop(0)  # Pop the first command from the queue
        print(f"first command '{command}' popped and added to the output.txt file")
        with open("dram.txt", "a") as file:
            file.write(command + "\n")  # Write the popped command to output file

# Display DRAM commands
for command in dram_commands_list:
    if is_queue_full(dram_queue):
        print("Queue is full.")
        pop_from_queue(dram_queue)
        dram_queue.append(command)
        wait = dram_commands_list[dram_commands_list.index(command):]
        if wait and wait[0].startswith("At this cpu time"):
            current_time = int(wait[0].split()[4])  # Extract the current time
            new_time = current_time + 32  # Increment time after 32 clock cycles
            wait[0] = f"At this cpu time {new_time} ns"  # Update the time in the wait state
        with open("dram2.txt", "a") as file:
            for cmd in dram_queue:
                file.write(cmd + "\n")  # Write the commands in the queue to output file
            for cmd in wait:
                file.write(cmd + "\n")  # Write the updated wait state to output file
        dram_queue = []  # Clear the queue
        break
    else:
        dram_queue.append(command)

# Write the remaining commands in the queue to output file
with open("dram2.txt", "a") as file:
    for cmd in dram_queue:
        file.write(cmd + "\n")



# # Write the remaining commands in the queue to output file
# while dram_queue:
#     pop_from_queue(dram_queue)

# Display commands in the queue and buffer
if __debug__ :
     pass
else:
    print(" queue information:")
    print(f"\n{dram_queue}")
    print(f"Size of the queue:{len(dram_queue)}")
        
    # print(dram_queue)

    print("Commands in the wait state:")
    print(wait)
    print(f"Size of the wait states:{len(wait)}")

