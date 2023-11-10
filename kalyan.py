def msd_trace_file(file_path="D:\\MSD_Project23\\output.txt"):
    with open(file_path, 'r') as file:
        lines = file.readline()
        for f in lines:
            cores = f.split('')
            print(cores)





user_specified_file = "D:\\MSD_Project23\\output.txt"
if user_specified_file:
   msd_trace_file(user_specified_file)
