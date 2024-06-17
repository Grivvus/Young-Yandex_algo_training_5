def build_a_square(n: int, points: list[tuple[int]]) -> list[int] | int:
    set_of_points = set(points)


if __name__ == "__main__":
    with open(
        "/home/grivvus/Py_Projects/YoungYandex/algo_training_5/task3/input.txt"
    ) as file:
        n = int(file.readline())
        points = []
        for i in range(n):
            points.append(tuple([int(i) for i in file.readline().split()]))
        ans = build_a_square(n, points)