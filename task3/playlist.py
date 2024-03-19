# Костя успешно прошел собеседование и попал на стажировку в отдел
# разработки сервиса «Музыка».
# Конкретно ему поручили такое задание — научиться подбирать плейлист
# для группы друзей, родственников или коллег. При этом нужно подобрать
# такой плейлист, в который входят исключительно нравящиеся всем
# членам группы песни.
# Костя очень хотел выполнить это задание быстро и качественно, но у него
# не получается. Помогите ему написать программу, которая составляет плейлист
# для группы людей.

def playlist(n: int, playlists: list[str]) -> list[str]:
    d = {}
    for i in playlists:
        for j in i:
            if j not in d:
                d[j] = 1
            else:
                d[j] += 1
    ans = []
    cnt = 0
    for i in d.keys():
        if d[i] == n:
            cnt += 1
            ans.append(i)
    ans.sort()
    print(cnt)
    return ans

if __name__ == "__main__":
    n = int(input())
    playlists = []
    for i in range(n):
        ln = int(input())
        playlists.append(input().split())
    print(*playlist(n, playlists))
