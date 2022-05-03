#https://www.beecrowd.com.br/judge/pt/problems/view/1030

def kill(grupo:list, mortes_da_rodada:list):
    for morte in mortes_da_rodada:
        if len(grupo) != 1:
            grupo.remove(morte)

qnt = input()
for _ in range(int(qnt)):
    n, k = list(map(int, input().split(' ')))
    pessoas = list(range(1,n+1))
    cnt = 0
    mortes = []
    while True:
        if cnt >= len(pessoas):
            cnt -= len(pessoas)
            if mortes:
                kill(pessoas, mortes)
                mortes = []
        else:
            cnt += k

        if len(pessoas) == 1:
            break

        if cnt == 0:
            cnt = 1

        mortes.append(pessoas[cnt-1])
    print(f"Case {_+1}: {pessoas[0]}")
