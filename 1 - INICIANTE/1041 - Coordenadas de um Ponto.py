#https://www.beecrowd.com.br/judge/pt/problems/view/1041

coord1, coord2 = map(float, input().split())
output = ""
if coord1 == 0.0:
    if coord2 == 0.0:
        output = 'Origem'
    if not output:
        output = 'Eixo Y'
if coord2 == 0.0 and not output:
    output = 'Eixo X'

if coord1 * coord2 > 0.0 and not output:
    if coord1 > 0.0 and coord2 > 0.0: # ou coord1+coord2 > coord1
        output = 'Q1'
    if not output:
        output = 'Q3'

if not output:
    if coord1 < 0.0: # ou coord1+coord2 > coord1
        output = 'Q2'
    if not output:
        output = 'Q4'

print(output)