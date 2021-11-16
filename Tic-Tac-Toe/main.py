
# Check is Valid
def check(m):


    # if Impossible when X or O is more than should be
    x = m.count("X")
    o = m.count("O")

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 'X':
                x += 1
            elif matrix[i][j] == 'O':
                o += 1
    if abs(x - o) > 1:
        return "Impossible"
    if x_check(matrix) and o_check(matrix):
        return "Impossible"
    if "_" in matrix[0] or "_" in matrix[1] or "_" in matrix[2]:
        if not x_check(matrix) and not o_check(matrix):
            return "Game not finished"
        elif x_check(matrix):
            return "X wins"
        else:
            return "O wins"
    else:
        if not x_check(matrix) and not o_check(matrix):
            return "Draw"
        elif x_check(matrix):
            return "X wins"
        else:
            return "O wins"


# X Wins check
def x_check(matrix):
    if matrix[0][0] == 'X' and matrix[0][1] == 'X' and matrix[0][2] == 'X':
        return True
    if matrix[1][0] == 'X' and matrix[1][1] == 'X' and matrix[1][2] == 'X':
        return True
    if matrix[2][0] == 'X' and matrix[2][1] == 'X' and matrix[2][2] == 'X':
        return True

    if matrix[0][0] == 'X' and matrix[1][1] == 'X' and matrix[2][2] == 'X':
        return True
    if matrix[0][2] == 'X' and matrix[1][1] == 'X' and matrix[2][0] == 'X':
        return True

    if matrix[0][0] == 'X' and matrix[1][0] == 'X' and matrix[2][0] == 'X':
        return True
    if matrix[0][1] == 'X' and matrix[1][1] == 'X' and matrix[2][1] == 'X':
        return True
    if matrix[0][2] == 'X' and matrix[1][2] == 'X' and matrix[2][2] == 'X':
        return True

    return False

# O Wins check
def o_check(matrix):
    if matrix[0][0] == 'O' and matrix[0][1] == 'O' and matrix[0][2] == 'O':
        return True
    if matrix[1][0] == 'O' and matrix[1][1] == 'O' and matrix[1][2] == 'O':
        return True
    if matrix[2][0] == 'O' and matrix[2][1] == 'O' and matrix[2][2] == 'O':
        return True

    if matrix[0][0] == 'O' and matrix[1][1] == 'O' and matrix[2][2] == 'O':
        return True
    if matrix[0][2] == 'O' and matrix[1][1] == 'O' and matrix[2][0] == 'O':
        return True

    if matrix[0][0] == 'O' and matrix[1][0] == 'O' and matrix[2][0] == 'O':
        return True
    if matrix[0][1] == 'O' and matrix[1][1] == 'O' and matrix[2][1] == 'O':
        return True
    if matrix[0][2] == 'O' and matrix[1][2] == 'O' and matrix[2][2] == 'O':
        return True

    return False
# Main
def main(matrix):
    print("---------")

    for i in range(len(matrix)):
        print("|", end=" ")
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print("|")

    print("---------")
def user_input(matrix):
    while True:
        try:
            a, b = map(int, input("Enter the coordinates: ").split())
            if not a in range(1, 4) or not b in range(1, 4):
                print("Coordinates should be from 1 to 3!")
            else:
                if matrix[a - 1][b - 1] == '_':
                    matrix[a - 1][b - 1] = 'X'
                    break
                else:
                    print("This cell is occupied! Choose another one!")
        except:
            print("You should enter numbers!")
    return None
# Setup
cells = list("_________")
matrix = []
temp = []
for i in range(9):
    if i == 2 or i == 5 or i == 8:
        temp.append(cells[i])
        matrix.append(temp)
        temp = []
    else:
        temp.append(cells[i])
move = True
while True:
    if check(matrix) != 'Game not finished':
        break
    user_input(matrix)




    break