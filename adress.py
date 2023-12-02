
#q = [88,89]
#l = input("enter a address:")

def file1(file_path="C:\\Users\\sripa\\OneDrive\\Desktop\\MSD_PROJECT\\project\\address.txt"):
        try:
                with open(file_path, 'r') as file:
                        for line in file:
                                print(line, end='')
                #                 for w in e:      
                #                         if w == l:
                #                                 print("address matched in queue")
                #                                 break
                # if w != l:
                #         i = input("enter a new address need to add into queue: ")
                #         file1.append(i)
                #         print("final added address:", file1)
                               
        except FileNotFoundError:
                print(f"Error: File '{file1}' not found.")


        # for w in e:      
        #         if w == l:
        #                 print("address matched in queue")
        #                 break
        # if w != l:
        #         i = input("enter a new address need to add into queue: ")
        #         file1.append(i)
        #         print("final added address:", file1)


           # l=[]
        # with open(file_name, 'r') as file:
        #     # Read and print each line
        #     for line in file:
        #         l.append(line)
        #         print(line, end='')
                
                


