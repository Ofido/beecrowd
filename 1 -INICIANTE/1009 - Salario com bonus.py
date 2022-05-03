#https://www.beecrowd.com.br/judge/pt/problems/view/1009

_ = input()
salario_fixo = float(input())
vendas = float(input())

print(f"TOTAL = R$ {((vendas * 0.15) + salario_fixo):.2f}")