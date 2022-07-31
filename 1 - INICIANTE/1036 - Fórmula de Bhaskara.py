#https://www.beecrowd.com.br/judge/pt/problems/view/1036
import math

a, b, c = map(float, input().split())
try:
    x = math.sqrt(math.pow(b, 2) - 4 * a * c)

    r1 = (-b + x) / (2 * a)
    r2 = (-b - x) / (2 * a)

    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")
except:
    print("Impossivel calcular")
