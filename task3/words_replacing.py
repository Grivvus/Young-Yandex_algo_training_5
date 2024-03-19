# С целью экономии чернил в картридже принтера было принято решение укоротить
# некоторые слова в тексте. Для этого был составлен словарь слов, до которых
# можно сокращать более длинные слова. Слово из текста можно сократить, если
# в словаре найдется слово, являющееся началом слова из текста. Например, если
# в списке есть слово "лом", то слова из текста "ломбард", "ломоносов" и другие
# слова, начинающиеся на "лом", можно сократить до "лом".
# Если слово из текста можно сократить до нескольких слов из словаря, то
# следует сокращать его до самого короткого слова.
def replacing(dictionary: list[str], text: list[str]) -> str:
    replacing = {}
    cnt = 0
    dictionary.sort(key=lambda x: len(x))
    for i in set(text):
        if cnt == len(text):
            break
        for j in dictionary:
            if i.startswith(j):
                if i not in replacing:
                    cnt += 1
                    replacing[i] = j
                else:
                    if len(replacing[i]) > len(j):
                        replacing[i] = j

    ans = []
    for i in text:
        if i in replacing:
            ans.append(replacing[i])
        else:
            ans.append(i)

    return ans

if __name__ == "__main__":
    with open(
        "/home/grivvus/Py_Projects/YoungYandex/algo_training_5/task3/input.txt"
    ) as file:
        dictionary = file.readline().split()
        text = file.readline().split()
        print(*replacing(dictionary, text))
