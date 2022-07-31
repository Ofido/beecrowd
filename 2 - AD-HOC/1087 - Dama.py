#https://www.beecrowd.com.br/judge/pt/problems/view/1087
#

while True:
    x1, y1, x2, y2 = list(map(int, input().split()))

    if x1 + y1 + x2 + y2 == 0:
        break

    resolucao = 0
    # verificando mesma linha
    if x1 == x2:
        if y1 == y2:
            resolucao = 1
        else:
            resolucao = 2

    if not resolucao:
        if y1 == y2:
            resolucao = 2
        else:
            if abs((y2 - y1) / (x2 - x1)) == 1:
                resolucao = 2
            else:
                resolucao = 3

    print(resolucao-1)