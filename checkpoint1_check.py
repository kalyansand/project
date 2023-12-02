import sys
#n = int(input("enter a debug_mode:"))
def print_file(file_name="C:\\Users\\sripa\\OneDrive\\Desktop\\MSD_PROJECT\\project\\kalyan.txt"):
    file = open(file_name, 'r')
    l1 = file.read()
    print(l1)

if __name__ == "__main__":

    if len(sys.argv)-1 > 1:
        pass

    if len(sys.argv)-1 == 0:
        print_file()
    else:
        file_name = sys.argv[1]
        print_file(file_name)
   
     