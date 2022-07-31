#https://www.beecrowd.com.br/judge/pt/problems/view/1030
#algoritimo esta correto, só esta demorando muito tempo

def escrever(msg1, msg2):
    msg2 = str(msg2)
    msg1 = str(msg1)
    with open("oi2.txt", 'a', encoding='utf8') as f:
        f.write(msg1+ " " +msg2+"\n")

def kill(grupo:list, mortes_da_rodada:list):
    for morte in mortes_da_rodada:
        if len(grupo) != 1:
            grupo.remove(morte)

qnt = input()
for _ in range(int(qnt)):
    n, k = list(map(int, input().split()))
    pessoas = list(range(1,n+1))
    cnt = 0
    mortes = []
    while len(pessoas) > 1:
        escrever(cnt, len(pessoas))
        if cnt > len(pessoas):
            cnt -= len(pessoas)
            if mortes:
                kill(pessoas, mortes)
                mortes = []
        else:
            cnt += k
        if cnt == 0:
            cnt = 1
        try:
            mortes.append(pessoas[cnt-1])
        except:
            pass
    print(f"Case {_+1}: {pessoas[0]}")
