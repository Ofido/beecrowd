#https://www.beecrowd.com.br/judge/pt/problems/view/1012
#

'''
    definindo sempre que para as funções do_[algo], que sempre dito A, B ou C; se trata de kwargs['medida_A'], kwargs['medida_B'] e kwargs['medida_C'], respectivamente.
'''

import math


def do_TRIANGULO(**kwargs) -> float:
    '''
        a área do triângulo retângulo que tem A por base e C por altura.
    '''
    return (kwargs['medida_A'] * kwargs['medida_C']) / 2

def do_CIRCULO(**kwargs) -> float:
    '''
        a área do círculo de raio C. (pi = 3.14159)
    '''
    return math.pow(kwargs['medida_C'], 2) * 3.14159

def do_TRAPEZIO(**kwargs) -> float:
    '''
        a área do trapézio que tem A e B por bases e C por altura.
    '''
    return ((kwargs['medida_A'] + kwargs['medida_B']) * kwargs['medida_C']) / 2

def do_QUADRADO(**kwargs) -> float:
    """
        a área do quadrado que tem lado B.
    """
    return math.pow(kwargs['medida_B'], 2)

def do_RETANGULO(**kwargs) -> float:
    """
        a área do retângulo que tem lados A e B.
    """
    return kwargs['medida_A'] * kwargs['medida_B']

medida_A, medida_B, medida_C = list(map(float, input().split(' ')))

for figura in [('TRIANGULO', do_TRIANGULO), ('CIRCULO', do_CIRCULO), ('TRAPEZIO', do_TRAPEZIO), ('QUADRADO', do_QUADRADO), ('RETANGULO', do_RETANGULO)]:
    print(f"{figura[0]}: {(figura[1](medida_A=medida_A, medida_B=medida_B, medida_C=medida_C)):.3f}")
