# -*- coding: utf-8 -*-
# https://www.beecrowd.com.br/judge/pt/problems/view/1066

resultado = {
    "pares": 0,
    "impares": 0,
    "positivos": 0,
    "negativos": 0
}

for _ in range(5):
    aux = int(input())
    if aux != 0:
        if aux > 0:
            resultado["positivos"] += 1
        else:
            resultado["negativos"] += 1
        
    if (aux % 2) == 0:
        resultado["pares"] += 1
    else:
        resultado["impares"] += 1
        
print(resultado["pares"],"valor(es) par(es)")
print(resultado["impares"],"valor(es) impar(es)")
print(resultado["positivos"],"valor(es) positivo(s)")
print(resultado["negativos"],"valor(es) negativo(s)")