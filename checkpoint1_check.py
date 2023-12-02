import sys
#n = int(input("enter a debug_mode:"))

def print_file_lines(file_name="C:\\Users\\sripa\\OneDrive\\Desktop\\MSD_PROJECT\\project\\kalyan.txt"):
    try:
        
        file = open(file_name, 'r')
        l1 = file.read()
        # l=[]
        # with open(file_name, 'r') as file:
        #     # Read and print each line
        #     for line in file:
        #         l.append(line)
        #         print(line, end='')
        
        with open('trace.txt', 'w') as file:
        #    # for line in l:
            file.write(l1)
            print("write completed")
        
                
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

def remove_content():
    file = open('trace.txt', 'w')
    file.write(" ")

def print_file(file_name="C:\\Users\\sripa\\OneDrive\\Desktop\\MSD_PROJECT\\project\\kalyan.txt"):
    file = open(file_name, 'r')
    l1 = file.read()
    print(l1)
# if n == 1:
#     print("debug mode : 1 indicates ON \n ")
#     print_file_lines()
# elif n == 0:
#     print("debug mode is off")
#     remove_content()
    
if __name__ == "__main__":

    if len(sys.argv)-1 > 1:
        pass

    if len(sys.argv)-1 == 0:
        print_file()
    else:
        file_name = sys.argv[1]
        print_file(file_name)
            
              


   
 
       
     