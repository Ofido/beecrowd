#https://www.beecrowd.com.br/judge/pt/problems/view/1329
# 0.103s

while True:
    n = int(input())

    if n == 0:
        break

    n = input().split(' ')

    # n = list(map(lambda x: x == "1", ))

    # 0 | False -> maria
    x = n.count("0")
    print(f"Mary won {x} times and John won {len(n)-x} times")
