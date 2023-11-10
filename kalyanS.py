with open('/Users/sandeepreddy/Desktop/kalyan/project/kalyan.txt', 'r') as file:
    for line in file:
        print(line, end='') 







# def msd_trace_file(file_path="/Users/sandeepreddy/Desktop/kalyan/project/kalyan.txt"):
#     with open(file_path, 'r') as file:
#         lines = file.readline()
#         print(lines)
#         for f in lines:
#             cores = f.split('')
#             print(cores)





# user_specified_file = "/Users/sandeepreddy/Desktop/kalyan/project/kalyan.txt"
# if user_specified_file:
#    msd_trace_file(user_specified_file)



import sys
#input_file = open("trace.txt", 'r')
if len(sys.argv) != 2:
    print("Usage: python split.py <input_file.txt>")
    sys.exit(1)
input_file = sys.argv[1]
try:
    with open(input_file, 'r') as file:
        content = file.read()
        print("Contents of the file:")
        print(content)
except FileNotFoundError:
    # print(str("Error: File  "+  input_file + "not found."))

