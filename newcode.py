import sys
import argparse

# Define a function to read and print lines from a file
def print_file_lines(file_name):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read and print each line
            for line in file:
                print(line, end='')  
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--filepath", type=str, default="kalyan.txt", help=" value should be file path")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    
    args = parser.parse_args()
    print(args.filepath)
    
    if args.debug==False:
        exit()
        
    else:
        print_file_lines(args.filepath)