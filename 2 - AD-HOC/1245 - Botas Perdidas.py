#https://www.beecrowd.com.br/judge/pt/problems/view/1245

class Bota():
    def __init__(self):
        self.pares:dict = {}

    def verifica(self, numero) -> None:
        if not self.pares.get(numero, []):
            self.pares[numero] = {"D": 0, "E": 0}
        pass

    def add_bota(self, numero:int, lado:str):
        self.verifica(numero)
        self.pares[numero][lado] += 1
        pass

    def pares_por_numero(self, par) -> int:
        d, e = list(self.pares[par].values()) # teeste sem list
        if d <= e:
            return d
        return e

    def conta_pares(self):
        total_de_pares = 0
        for par in list(self.pares):
            total_de_pares += self.pares_por_numero(par)
        return total_de_pares

    def __str__(self) -> str:
        return str(self.conta_pares())

while True:
    try:
        qnt = input()

        botas = Bota()

        for bota in range(int(qnt)):
            numero, lado = input().split(' ')
            botas.add_bota(int(numero), lado)

        print(botas)
    except EOFError:
        break