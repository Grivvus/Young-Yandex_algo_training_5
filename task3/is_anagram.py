# Задано две строки, нужно проверить, является ли одна анаграммой другой.
# Анаграммой называется строка, полученная из другой перестановкой букв.

def is_anagram(s1: str, s2: str) -> bool:
    d1 = {}
    d2 = {}
    for i in s1:
        if i not in d1:
            d1[i] = 1
        else:
            d1[i] += 1

    for i in s2:
        if i not in d2:
            d2[i] = 1
        else:
            d2[i] += 1
    if d1 == d2:
        return True
    return False

if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print("YES") if is_anagram(s1, s2) else print("NO")