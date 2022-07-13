#https://www.beecrowd.com.br/judge/pt/problems/view/1018

notas_disponiveis:list[int]  = [100, 50, 20, 10, 5, 2, 1]

def dinheiro_em_cedula(valor: int):
    print(valor)
    for nota in notas_disponiveis:
        qnt, valor = divmod(valor, nota)
        print(f"{qnt} nota(s) de R$ {nota},00")

dinheiro_em_cedula(int(input()))