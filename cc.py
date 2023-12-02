# Address mapping function (unchanged)
import sys


tCL = 40
tRC = 115
tRAS =76
tRRD_L =12
tRRD_S =8
tRP =39
tRFC =295
tCL =40
tCWD =38
tRCD =39
tWR =30
tRTP =18
tCCD_L= 12
tCCD_S= 8
tCCD_L_WR= 48
tCCD_S_WR =8
tBURST =8
tCCD_L_RTW= 16
tCCD_S_RTW =16
tCCD_L_WTR =70
tCCD_S_WTR =52
def address_mapping(address):
    binary_address = bin(int(address, 16))[2:].zfill(34)
    low_column = hex(int(binary_address[-6:-2], 2))[2:]
    bank_group = int(binary_address[-10:-7], 2)
    bank = int(binary_address[-12:-10], 2)
    row = hex(int(binary_address[-18:-12], 2))
    column = hex(int(binary_address[:-18], 2))
    #return bank_group, bank, column, row
    # print(f' binary address of memory request : {memory_request_address}')
    # print(f'{binary_address}')
    # print(f"Below is address mapping info")
    # print(f"low_column:{low_column}")
    # print(f"Bank_group: {bank_group}")
    # print(f"Bank: {bank}")
    # print(f"Column: {column}")
    # print(f"Row: {row}")
    return (low_column,bank_group,bank,column,row)
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
            
            # print(memory_requests)
    return memory_requests

# Generate DRAM commands based on memory operation type
def generate_dram_commands(memory_requests):
    dram_commands = []
    channel = 0
    t3 = 0
    temp_bank = 5
    temp_bankgroup = 9
    
    for request in memory_requests:
        time = request["time"]
       # core = request["core"]
        operation = request["operation"]
        addresses = request["address"]
        
        low_column, bank_group, bank, column, row = address_mapping(addresses)  # Call address_mapping for each address
        # print(f"{low_column},{bank_group},{bank}, {column},{row}")
        # print("bank, bankgroup, prev:-------", bank_group, bank)
        # print("prev, prev_bank---", prev_bankgroup, prev_bank)
       
        if bank_group != temp_bankgroup and bank != temp_bank:
            t1 = t3 + 1
            t2 = t1 + tRCD
            t3 = t2 + tCL + tBURST
            if operation == 0 or operation == 2:
                dram_commands.append(f"{t1*2} {channel} ACT0 {bank_group} {bank} {row}")
                dram_commands.append(f"{t1*2} {channel} ACT1 {bank_group} {bank} {row}")
                dram_commands.append(f"{t2*2} {channel} RD0  {bank_group} {bank} {column}{low_column}")
                dram_commands.append(f"{t2*2} {channel} RD1  {bank_group} {bank} {column}{low_column}")
                dram_commands.append(f"{t3*2} {channel} PRE  {bank_group} {bank} \n")
            elif operation == 1:
                dram_commands.append(f"{t1*2} {channel} ACT0 {bank_group} {bank} {row}")
                dram_commands.append(f"{t1*2+2} {channel} ACT1 {bank_group} {bank} {row}")
                dram_commands.append(f"{t2*2+tCWD+tWR} {channel} WR0  {bank_group} {bank} {column}{low_column}")
                dram_commands.append(f"{t2*2+tCWD+tWR+2} {channel} WR1  {bank_group} {bank} {column}{low_column}")
                dram_commands.append(f"{t3*2} {channel} PRE  {bank_group} {bank} \n")       
        elif bank_group == temp_bankgroup and bank == temp_bank:
            t1 = t3 + 1 + tRP
            t2 = t1 + tRCD
            t3 = t2 + tCL + tBURST
            if operation == 0 or operation == 2:
                dram_commands.append(f"{t1*2} {channel} ACT0 {bank_group} {bank} {row}")
                dram_commands.append(f"{t1*2} {channel} ACT1 {bank_group} {bank} {row}")
                dram_commands.append(f"{t2*2} {channel} RD0  {bank_group} {bank} {column}{low_column}")
                dram_commands.append(f"{t2*2} {channel} RD1  {bank_group} {bank} {column}{low_column}")
                dram_commands.append(f"{t3*2} {channel} PRE  {bank_group} {bank} \n")
            elif operation == 1:
                dram_commands.append(f"{t1*2} {channel} ACT0 {bank_group} {bank} {row}")
                dram_commands.append(f"{t1*2} {channel} ACT1 {bank_group} {bank} {row}")
                dram_commands.append(f"{t2*2} {channel} WR0  {bank_group} {bank} {column}{low_column}")
                dram_commands.append(f"{t2*2} {channel} WR1  {bank_group} {bank} {column}{low_column}")
                dram_commands.append(f"{t3*2} {channel} PRE  {bank_group} {bank} \n")   
        temp_bankgroup = bank_group
        temp_bank = bank
        # print (f"{prev_bankgroup},{prev_bank}")
        #ck_time =0
    # print(dram_commands)
    return dram_commands

# Rest of the code remains unchanged

# Input trace file
input_file = input ("Enter any test file ") or "tracecp2.txt"  # Replace with your input file name

with open("dram.txt", "w") as file:
            file.write('')
# Read input trace file
input_requests = read_input_trace(input_file)




# Check if the queue is full
def is_queue_full(queue):
    return len(queue) >= 16
# Generate DRAM commands for all requests
dram_commands_list = generate_dram_commands(input_requests)
# Define a queue to hold the DRAM commands
dram_queue = []
wait = []
# Function to pop from queue and write to output file
# def pop_from_queue(queue):
#     if queue:
#         command = queue.pop(0)  # Pop the first command from the queue
#         print(f"first command '{command}' popped and added to the output.txt file")
#         with open("dram1.txt", "a") as file:
#             file.write(command + "\n")  # Write the popped command to output file

# Display DRAM commands
for command in dram_commands_list:
    if not is_queue_full(dram_queue):
        dram_queue.append(command)
    else:
        wait = dram_commands_list[dram_commands_list.index(command):]
        break 
# else:
#         
#         dram_queue.append(command)  # Append the command to the queue
with open('dram.txt', 'w') as file:
    file.writelines(command + "\n" for command in dram_queue + wait)


# # Write the remaining commands in the queue to output file
# while dram_queue:
#     pop_from_queue(dram_queue)

# Display commands in the queue and buffer

# print(" queue information:")
#print(f"\n{dram_queue}")
print(f"Size of the queue:{len(dram_queue)}")
    
# print(dram_queue)

#print("Commands in the wait state:")
#print(wait)
print(f"Size of the wait states:{len(wait)}")
print(f"length of instructions: {len(dram_queue)+len(wait)}")