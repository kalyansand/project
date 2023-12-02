from collections import deque

# Initialize necessary data structures
queue = deque()  # Memory request queue
time = 0  # Current simulated time

# Default filenames
input_trace_filename = "trace.txt"
output_filename = "dram.txt"

# Simulated processor clock speed
processor_clock_cycles = 1  # You might adjust this based on your requirements

# Input trace file handling
input_trace_filename = input("Enter the input trace file name (default: trace.txt): ").strip() or "trace.txt"
output_filename = input("Enter the output file name (default: dram.txt): ").strip() or "dram.txt"

# Clear the existing content of the output file
with open(output_filename, 'w') as file:
    file.write("")

# Read and parse input trace file
with open(input_trace_filename, 'r') as input_file:
    for line in input_file:
        time, core, operation, address = map(str.strip, line.split())

        # Insert memory request into the queue
        memory_request = {'time': time, 'core': core, 'operation': int(operation), 'address': address}
        queue.append(memory_request)

        # Simulate processor clock cycles
        time = int(time) + processor_clock_cycles

        # Issue DRAM commands
        if queue:
            next_request = queue.popleft()
            if next_request['operation'] == 0:
                dram_commands = ['ACT0', 'RD0']
            elif next_request['operation'] == 1:
                dram_commands = ['ACT0', 'WR0']
            elif next_request['operation'] == 2:
                dram_commands = ['ACT0', 'RD0']
            else:
                dram_commands = ['NO', 'OUTPUT']

            # Output DRAM commands to the file
            with open(output_filename, 'a') as file:
                for command in dram_commands:
                    print(command,time)
                    file.write(f"{time} {command}\n")


print('completed')