import sys

# Define a function to read and print lines from a file
def print_file_lines(file_name="/Users/sandeepreddy/Desktop/kalyan/project/kalyan.txt"):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read and print each line
            for line in file:
                print(line, end='')  # 'end='' to avoid double spacing due to newline characters
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")



if __name__ == "__main__":
    # will use when we give multiple files 
    if len(sys.argv) > 1:
        print("Usage: python3 xxx.py <file_name>")


    # Get the file name from the command line argument
    # file_name = sys.argv[1]

    # # Call the function to print file lines
    # print_file_lines(file_name)
    
    
    if len(sys.argv) == 1:
        print_file_lines()
    else:
        file_name = sys.argv[1]
        print_file_lines(file_name)
        