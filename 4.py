LIM_CNT = 125
DIAG_X = 11#84+36=120/12=10+1=11
DIAG_Y = 7
with open("sequence.txt") as txt_file:
    cnt_of_num = 0
    cnt = 0
    sum_0_125 = 0
    sum_126_250 = 0
    for number in txt_file:
        number = number.replace("\n", '')
        number = eval(number)
        cnt += 1
        if cnt < LIM_CNT:
            sum_0_125 += number
        else:
            sum_126_250 += number
print(sum_0_125)
print(sum_126_250)
diag_250 = [[0, 0, 0, 3, 3, 3, 3],
            [0, 0, 0, 3, 3, 3, 3],
            [0, 0, 0, 3, 3, 3, 3],
            [0, 0, 0, 3, 3, 3, 3],
            [0, 0, 0, 3, 3, 3, 3],
            [0, 0, 0, 3, 3, 3, 3],
            [0, 0, 0, 3, 3, 3, 3],
            [1, 1, 1, 3, 1, 1, 1],
            [3, 3, 3, 3, 2, 2, 2],
            [3, 3, 3, 3, 2, 2, 2],
            [3, 3, 3, 3, 2, 2, 2]]

for string in range(DIAG_X):
    for column in range(DIAG_Y):
        if diag_250[string][column] == 0:
            print("\x1b[31m", end='')
            print("#", end="")
        elif diag_250[string][column] == 1:
            print("\x1b[32m", end='')
            print("#", end="")
        elif diag_250[string][column] == 2:
            print("\x1b[35m", end='')
            print("#", end="")
        else:
            print(' ', end='')
    print('\t')
