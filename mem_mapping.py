# Address mapping function (unchanged)
def address_mapping(memory_request_address):
    binary_address = bin(int(memory_request_address, 16))[2:].zfill(34)
    bank_group = int(binary_address[-10:-7], 2)
    bank = int(binary_address[-12:-10], 2)
    row = hex(int(binary_address[:-18], 2))
    column = hex(int(binary_address[-18:-12], 2))
    #return bank_group, bank, row, column
    print(f' binary address of memory request : {memory_request_address}')
    print(f'{binary_address}')
    print(f"Below is address mapping info")
    print(f"Bank_group: {bank_group}")
    print(f"Bank: {bank}")
    print(f"Column: {column}")
    print(f"Row: {row}")

    return (bank_group,bank,column,row)
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
    dim_time = 0
    channel = 0

    for request in memory_requests:
        time = request["time"]
        operation = request["operation"]
        address = request["address"]
        
        bank_group, bank, row, column = address_mapping(address)
        
        if operation == 0 or operation == 2:
            
            dram_commands.append(f"{dim_time} {channel} ACT0 {bank_group} {bank} {row}")
            dim_time += 104
            dram_commands.append(f"{dim_time} {channel} ACT1 {bank_group} {bank} {row}")
            dim_time += 107
            dram_commands.append(f"{dim_time} {channel} RD0  {bank_group} {bank} {column}")
            dim_time += 200
            dram_commands.append(f"{dim_time} {channel} RD1  {bank_group} {bank} {column}")
            dim_time += 100
            dram_commands.append(f"{dim_time} {channel} PRE  {bank_group} {bank}")
            dim_time += 100
        elif operation == 1:
            
            dram_commands.append(f"{dim_time} {channel} ACT0 {bank_group} {bank} {row}")
            dim_time += 120
            dram_commands.append(f"{dim_time} {channel} ACT1 {bank_group} {bank} {row}")
            dim_time += 130
            dram_commands.append(f"{dim_time} {channel} WR0  {bank_group} {bank} {column}")
            dim_time += 190
            dram_commands.append(f"{dim_time} {channel} WR1  {bank_group} {bank} {column}")
            dim_time += 200
            dram_commands.append(f"{dim_time} {channel} PRE  {bank_group} {bank}")
            dim_time += 100
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
        response = input("Do you want to pop from queue? (yes/no): ")
        if response.lower() == "yes":
            pop_from_queue(dram_queue)
            dram_queue.append(command)
            print(f"command '{command}' wait state pushed into the queue") 
        else:
            wait = dram_commands_list[dram_commands_list.index(command):]  # Store remaining commands
            break  # Exit loop if the user doesn't want to pop a command
    else:
        dram_queue.append(command)  # Append the command to the queue

# # Write the remaining commands in the queue to output file
# while dram_queue:
#     pop_from_queue(dram_queue)

# Display commands in the queue and buffer
print(" queue information:")
print(f"\n{dram_queue}")
print(f"Size of the queue:{len(dram_queue)}")
    
# print(dram_queue)

print("Commands in the wait state:")
print(wait)

