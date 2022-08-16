#https://www.beecrowd.com.br/judge/pt/problems/view/2867

'''
    Nota: a biblioteca math tem algum erro quando se trata números muito grandes.
    CUIDADO AO TRANSFORMAR NÚMEROS GRANDES EM FLOAT
'''

qnt = input()
for _ in range(int(qnt)):
    n, m = list(map(int, input().split()))
    print(len(f"{(n**m)}"))
