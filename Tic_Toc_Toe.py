# A tic toc game by me

print('Welcome to the Tic Toc Toe game ')


print(f'\t1  2  3\n\t4  5  6 \n\t7  8  9 ')
play = 1

lis = [1, 2, 3, 4, 5, 6, 7, 8, 9]


fill = 0


def marked(P):
    print()
    global fill
    # count = 0
    for i in (lis):
        if P == (i):
            # lis.insert(i, 'X')
            if turn == 1:
                lis[i - 1] = 'X'
                print(fill)
                fill += 1
            else:
                lis[i - 1] = 'O'
                fill += 1

    nl = '\n'
    space = '                            '
    print(f"{space}| {lis[0]} | {lis[1]} | {lis[2]} |{nl} {nl}{space}| {lis[3]} | {lis[4]} | {lis[5]} | {nl} {nl}{space}| {lis[6]} | {lis[7]} | {lis[8]} | ")
    print(fill)
    if fill == 9:
        print('No Blank Space left, please quit the game')


def compare():
    if ((lis[0] == 'X') and (lis[1] == 'X') and (lis[2] == 'X')):
        print(f'Bingo! \n{name_x} won the game, He was playing with X ')
        return 0
    if(lis[3] == 'X' and lis[4] == 'X' and lis[5] == 'X'):
        print(f'Bingo! \n{name_x} won the game, He was playing with X ')
        return 0
    if (lis[6] == 'X' and lis[7] == 'X' and lis[8] == 'X'):
        print(f'Bingo! \n{name_x} won the game, He was playing with X')
        return 0
    if ((lis[0] == 'X') and (lis[3] == 'X') and (lis[6] == 'X')):
        print(f'Bingo! \n{name_x} won the game, He was playing with X ')
        return 0

    if(lis[1] == 'X' and lis[4] == 'X' and lis[7] == 'X'):
        print(f'Bingo! \n{name_x} won the game, He was playing with X ')
        return 0
    if (lis[2] == 'X' and lis[5] == 'X' and lis[8] == 'X'):
        print(f'Bingo! \n{name_x} won the game, He was playing with X ')
        return 0
    if (lis[0] == 'X' and lis[4] == 'X' and lis[8] == 'X'):
        print(f'Bingo! \n{name_x} won the game, He was playing with X ')
        return 0
    if (lis[6] == 'X' and lis[4] == 'X' and lis[2] == 'X'):
        print(f'Bingo! \n{name_x} won the game, He was playing with X ')
        return 0

    if ((lis[0] == 'O') and (lis[1] == 'O') and (lis[2] == 'O')):
        print(f'Bingo! \n{name_y} won the game, was playing with O ')
        return 0

    if(lis[3] == 'O' and lis[4] == 'O' and lis[5] == 'O'):
        print(f'Bingo! \n{name_y} won the game, was playing with O ')
        return 0
    if(lis[2] == 'O' and lis[4] == 'O' and lis[6] == 'O'):
        print(f'Bingo! \n{name_y} won the game, He was playing with O ')
        return 0
    if (lis[6] == 'O' and lis[7] == 'O' and lis[8] == 'O'):
        print(f'Bingo! \n{name_y} won the game, He was playing with O ')
        return 0
    if (lis[0] == 'O') and (lis[3] == 'O') and (lis[6] == 'O'):
        print(f'Bingo! \n{name_y} won the game, He was playing with O ')
        return 0

    if(lis[1] == 'O' and lis[4] == 'O' and lis[7] == 'O'):
        print(f'Bingo! \n{name_y} won the game, He was playing with O ')
        return 0
    if (lis[2] == 'O' and lis[5] == 'O' and lis[8] == 'O'):
        print(f'Bingo! \n{name_y} won the game, He was playing with O ')
        return 0
    if (lis[0] == 'O' and lis[4] == 'O' and lis[8] == 'O'):
        print(f'Bingo! \n{name_y} won the game, He was playing with O ')
        return 0
    if (lis[6] == 'O' and lis[4] == 'O' and lis[2] == 'O'):
        print(f'Bingo! \n{name_y} won the game, He was playing with O ')
        return 0


name_x = input('Enter Name of first player : ')
name_y = input('Enter Name of Second player : ')
global x_function
while True:
    try:
        x = int(input(f'\n{name_x} turn to make a X , Press number where you want to Mark - \n'))
        turn = 1
        marked(x)
    except ValueError:
        pass
    x_function = compare()
    if x_function == 0:
        break
    try:
        y = int(input(f'\n{name_y} turn to make a O , Press number where you want to Mark - \n'))
        turn = 2
        marked(y)
    except ValueError:
        pass
    x_function = compare()
    if x_function == 0:
        break
