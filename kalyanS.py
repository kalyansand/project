with open('/Users/sandeepreddy/Desktop/kalyan.txt', 'r') as file:
    for line in file:
        print(line, end='')  # end='' to avoid double new lines when printing
