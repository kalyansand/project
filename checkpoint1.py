import sys
print("Debug mode 1 defines : ON \n Debug mode 0 defines : OFF \n Debug mode 2 defines : printing new file data")
n = int(input("enter a debug_mode:"))
def print_file_lines(file_name="C:\\Users\\sripa\\OneDrive\\Desktop\\MSD_PROJECT\\project\\kalyan.txt"):
    try:
        file = open(file_name, 'r')
        l1 = file.read()
        file = open('trace.txt', 'w')
        file.write(l1)
        print("created a trace.txt file and dumped the default file data")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
def remove_content():
    file = open('trace.txt', 'w')
    file.write(" ")
def print_file():
    file = open(file_name, 'r')
    l1 = file.read()
    print(l1)
if __name__ == "__main__":
            if n == 1:
                print("debug mode : 1 indicates ON \n ")
                print_file_lines()
            elif n == 0:
                print("debug mode is off")
                remove_content()
            elif n == 2:
                file_name = sys.argv[1]
                print("Printing the new file data")
                print_file()
                



            
              


   
 
       
     