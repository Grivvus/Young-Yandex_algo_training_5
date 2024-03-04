# На шахматной доске стоят слоны и ладьи, необходимо посчитать,
# сколько клеток не бьется ни одной из фигур.
# Шахматная доска имеет размеры 8 на 8. Ладья бьет все клетки горизонтали
# и вертикали, проходящих через клетку, где она стоит, до первой
# встретившейся фигуры. Слон бьет все клетки обеих диагоналей,
# проходящих через клетку, где он стоит, до первой встретившейся фигуры.

def r_go_upper(field, i, j):
    i -= 1
    while i >= 0 and field[i][j] != "B" and field[i][j] != "R":
        field[i][j] = "r"
        i -= 1

def r_go_down(field, i, j):
    i += 1
    while i <= 7 and field[i][j] != "B" and field[i][j] != "R":
        field[i][j] = "r"
        i += 1

def r_go_left(field, i, j):
    j -= 1
    while j >= 0 and field[i][j] != "B" and field[i][j] != "R":
        field[i][j] = "r"
        j -= 1

def r_go_right(field, i, j):
    j += 1
    while j <= 7 and field[i][j] != "B" and field[i][j] != "R":
        field[i][j] = "r"
        j += 1


def b_go_lu(field, i, j):
    i -= 1
    j -= 1
    while i >= 0 and j >= 0 and field[i][j] != "B" and field[i][j] != "R":
        field[i][j] = "b"
        i -= 1
        j -= 1
def b_go_ld(field, i, j):
    i += 1
    j -= 1
    while i <= 7 and j >= 0 and field[i][j] != "B" and field[i][j] != "R":
        field[i][j] = "b"
        i += 1
        j -= 1

def b_go_ru(field, i, j):
    i += 1
    j += 1
    while i <= 7 and j <= 7 and field[i][j] != "B" and field[i][j] != "R":
        field[i][j] = "b"
        i += 1
        j += 1

def b_go_rd(field, i, j):
    i -= 1
    j += 1
    while i >= 0 and j <= 7 and field[i][j] != "B" and field[i][j] != "R":
        field[i][j] = "b"
        i -= 1
        j += 1

def count_save_points(field: list[list[str]]) -> int:
    for i in range(8):
        for j in range(8):
            if field[i][j] == "B":
                b_go_lu(field, i, j)
                b_go_ld(field, i, j)
                b_go_ru(field, i, j)
                b_go_rd(field, i, j)
            elif field[i][j] == "R":
                r_go_down(field, i, j)
                r_go_upper(field, i, j)
                r_go_left(field, i, j)
                r_go_right(field, i, j)
            else:
                continue
    sum_ = 0
    for i in field:
        sum_ += i.count("*")
    return sum_


def print_(field: list[list[str]]):
    for i in field:
        for j in i:
            print(j, end="")
        print()

if __name__ == "__main__":
    field = []
    with open(
        "input.txt"
    ) as f:
        for i in range(8):
            string = []
            s = f.readline()[:8]
            for i in s:
                string.append(i)
            field.append(string)
    print(count_save_points(field))