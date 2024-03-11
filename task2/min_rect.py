# На клетчатой плоскости закрашено K клеток. Требуется найти минимальный
# по площади прямоугольник, со сторонами, параллельными линиям сетки,
# покрывающий все закрашенные клетки.

if __name__ == "__main__":
    n = int(input())
    x = [int(i) for i in input().split()]
    min_x = x[0]
    max_x = x[0]
    min_y = x[1]
    max_y = x[1]
    for i in range(n-1):
        x = [int(i) for i in input().split()]
        if x[0] > max_x:
            max_x = x[0]
        elif x[0] < min_x:
            min_x = x[0]

        if x[1] > max_y:
            max_y = x[1]
        elif x[1] < min_y:
            min_y = x[1]

    print(min_x, min_y, max_x, max_y)
