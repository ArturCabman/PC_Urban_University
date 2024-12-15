def check_winner():
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[3][0] == 'X' and area[3][1] == 'X' and area[3][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[2][0] == 'X' and area[3][0] == 'X':
        return 'X'
    if area[1][1] == 'X' and area[2][1] == 'X' and area[3][1] == 'X':
        return 'X'
    if area[1][2] == 'X' and area[2][2] == 'X' and area[3][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[2][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[1][2] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0':
        return '0'
    if area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0':
        return '0'
    if area[3][0] == '0' and area[3][1] == '0' and area[3][2] == '0':
        return '0'
    if area[1][0] == '0' and area[2][0] == '0' and area[3][0] == '0':
        return '0'
    if area[1][1] == '0' and area[2][1] == '0' and area[3][1] == '0':
        return '0'
    if area[1][2] == '0' and area[2][2] == '0' and area[3][2] == '0':
        return '0'
    if area[1][0] == '0' and area[2][1] == '0' and area[1][2] == '0':
        return '0'
    if area[1][2] == '0' and area[2][1] == '0' and area[2][2] == '0':
        return '0'
    return '*'

def draw_area():
    for i in area:
        print(*i)
area = [[], [' *', ' *', ' *'], [' *', ' *', ' *'], [' *', ' *', ' *'], []]
print('Добро пожаловать в крестики-нолики!')
print('-----------------------------------')
draw_area()
num_row = [1, 2, 3]
for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = ' 0'
        print('Ходят нолики')
    else:
        turn_char = ' X'
        print('Ходят крестики')
    row = int(input('Введите номер строки '))
    if row in num_row:
        column = int(input('Введите номер столбца ')) - 1
    else:
        print('Вы ввели неверное значение, пропуск хода')
        draw_area()
        continue
    if area[row][column] == ' *':
        area[row][column] = turn_char
    else:
        print('Ячейка занята, пропуск хода!')
        draw_area()
        continue

    if check_winner() == 'X':
        print('Победа крестиков')
        break
    if check_winner() == '0':
        print('Победа ноликов')
        break
    if check_winner() == '*' and turn == 9:
        print('Ничья')
        break
    else:
        draw_area()