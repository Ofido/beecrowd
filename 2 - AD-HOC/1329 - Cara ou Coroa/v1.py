#https://www.beecrowd.com.br/judge/pt/problems/view/1329
# 0.118s

while True:
    n = int(input())

    if n == 0:
        break

    n = list(map(lambda x: x == "1", input().split()))

    # 0 | False -> maria
    x = n.count(False)
    print(f"Mary won {x} times and John won {len(n)-x} times")
