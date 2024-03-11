# На столе лежали две одинаковые верёвочки целой положительной длины.
# Петя разрезал одну из верёвочек на N частей, каждая из которых имеет
# целую положительную длину, так что на столе стало N+1 верёвочек.
# Затем в комнату зашла Маша и взяла одну из лежащих на столе верёвочек.
# По длинам оставшихся на столе N верёвочек определите, какую наименьшую длину
# может иметь верёвочка, взятая Машей.


def find_last_min(data: list[int]) -> int:
    if len(data) == 1:
        return data[0]
    sm = 0
    max_cord = max(data)
    for i in range(len(data)):
        sm += data[i]

    if sm - max_cord == max_cord:
        return max_cord * 2
    if (sm - max_cord) - max_cord > 0:
        return sm
    return max_cord - (sm - max_cord)


if __name__ == "__main__":
   n = int(input())
   data = [int(i) for i in input().split()]
   print(find_last_min(data))
