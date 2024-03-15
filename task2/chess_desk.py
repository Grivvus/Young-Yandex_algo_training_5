# Из шахматной доски по границам клеток выпилили связную
# (не распадающуюся на части) фигуру без дыр. Требуется определить ее периметр.

def calc_perimeter(coords: list):
    sum_ = 0
    for i in coords:
        neighb = 0
        if [i[0], i[1]+1] in coords:
            neighb += 1
        if [i[0], i[1]-1] in coords:
            neighb += 1
        if [i[0]+1, i[1]] in coords:
            neighb += 1
        if [i[0]-1, i[1]] in coords:
            neighb += 1
        sum_ += (4-neighb)

    return sum_


if __name__ == "__main__":
    n = int(input())
    all_coords = []
    for i in range(n):
        all_coords.append([int(i) for i in input().split()])
    print(calc_perimeter(all_coords))