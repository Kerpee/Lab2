number_of_rep = int(input("Введите количество повторений узора:"))
SIZE_OF_PATTERN_X = 5
SIZE_OF_PATTERN_Y = 6*number_of_rep
pattern = [[1, 1, 1, 1, 0, 0]*number_of_rep,
           [1, 0, 0, 1, 0, 0]*number_of_rep,
           [1, 0, 1, 1, 0, 0]*number_of_rep,
           [1, 0, 1, 0, 0, 0]*number_of_rep,
           [1, 0, 1, 1, 1, 1]*number_of_rep]
for string in range(SIZE_OF_PATTERN_X):
    for column in range(SIZE_OF_PATTERN_Y):
        if pattern[string][column] == 1:
            print("\x1b[31m", end='')
            print("#", end='')
        else:
            print("\x1b[39m", end='')
            print("#", end='')
    print("\t")
