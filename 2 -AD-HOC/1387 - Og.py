#https://www.beecrowd.com.br/judge/pt/problems/view/1387

while True:
    n, k = list(map(int, input().split(' ')))
    if n == 0 :
        break
    else:
        print(n + k)
