number_of_rep=input("")
pattern = [[1, 1, 1, 1, 0, 0],
           [1, 0, 0, 1, 0, 0],
           [1, 0, 1, 1, 0, 0],
           [1, 0, 1, 0, 0, 0],
           [1, 0, 1, 1, 1, 1]]
for i in range(int(number_of_rep)):
    for string in range(5):
        for column in range(6):
            if pattern[string][column] == 1:
                print("\x1b[31m",end='')
                print("#",end='')
            else:
                print("\x1b[39m",end='')
                print("#",end='')
        print("\t")

