#https://www.beecrowd.com.br/judge/pt/problems/view/1837

# desisti deste desafio pelo fato do arredondamento do python para número negativo ser ao contrário
# a resposta correta seria usar o while igual ao 1021.

a, b = list(map(int, input().split()))
q, r = divmod(a, b)
# não precisa arrumar já que são dois números inteiros
# r = round(r, 2) # para arrumar o problema de base 2 e base 10
print(f"{q} {r}")
