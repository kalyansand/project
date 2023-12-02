import sys

# Define a function to read and print lines from a file
def print_file_lines(file_name="C:\\Users\\sripa\\OneDrive\\Desktop\\MSD_PROJECT\\project\\kalyan.txt", debug=False):
    try:
        # Open the file in read mode
        with open(file_name, 'r') as file:
            # Read and print each line
            for line in file:
                print(line, end='')
                
            # Print a debug message if debug mode is on
            if debug:
                print(f"\n[DEBUG] File '{file_name}' successfully read.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

if "_name_" == "_main_":
    # Default values
    file_name = "C:\\Users\\sripa\\OneDrive\\Desktop\\MSD_PROJECT\\project\\kalyan.txt"
    debug_mode = input("Enter debug mode:(ON/OFF)")

    # Check command-line arguments
    if len(sys.argv) > 1:
        # Check for debug flag
        if "--debug" in sys.argv:
            debug_mode = True

        # Check for a specified file name
        if len(sys.argv) > 2 and "--debug" not in sys.argv:
            file_name = sys.argv[2]

    # Call the function with the specified parameters
    print_file_lines(file_name,debug_mode)