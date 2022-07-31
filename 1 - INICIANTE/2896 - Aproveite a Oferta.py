#https://www.beecrowd.com.br/judge/pt/problems/view/2896

qnt = input()
for _ in range(int(qnt)):
    n, k = list(map(int, input().split()))
    if(n >= k):
        aux1 = n // k
        aux2 = n % k
        print(aux1+aux2)
    else:
        print(n)
