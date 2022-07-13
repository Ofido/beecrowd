#https://www.beecrowd.com.br/judge/pt/problems/view/1021

notas_disponiveis  = [100.00, 50.00, 20.00, 10.00, 5.00, 2.00]
moedas_disponiveis = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

def retirando_nota_por_nota(valor_restante:float, nota:float):
    """função baseada em while retirando nota por nota levando em consideração que o python não é bom em fazer divisões de números decimais usuais. (https://docs.python.org/3/tutorial/floatingpoint.html)

    Args:
        valor_restante (float): valor total restante
        nota (float): valor da cedula para ser retirado do montante total

    Returns:
        qnt: quantidade  de notas retiradas
        valor_restante: quantidade de dinheiro que ainda resta
    """
    qnt = 0
    while valor_restante >= nota:
        qnt += 1
        valor_restante = round(valor_restante - nota, 2)

    return qnt, valor_restante

def dinheiro_em_cedula(valor: float):
    print("NOTAS:")
    for nota in notas_disponiveis:
        # usando o método de subtração
        # qnt, valor = retirando_nota_por_nota(valor, nota)
        # usando o divmod
        qnt, valor = divmod(valor, nota)
        valor = round(valor, 2) # para arrumar o problema de base 2 e base 10
        print(f"{qnt:.0f} nota(s) de R$ {nota:.2f}")
    print("MOEDAS:")
    for moeda in moedas_disponiveis:
        # usando o método de subtração
        # qnt, valor = retirando_nota_por_nota(valor, moeda)
        # usando o divmod
        qnt, valor = divmod(valor, moeda)
        valor = round(valor, 2) # para arrumar o problema de base 2 e base 10
        # TODO bug de base para a moeda de 1 centavo ainda continua
        if valor > 0 and moeda == 0.01:
            qnt += 1
            valor = 0
        print(f"{qnt:.0f} moeda(s) de R$ {moeda:.2f}")

dinheiro_em_cedula(float(input()))