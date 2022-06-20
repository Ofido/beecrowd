A = None
B = None
C = None
D = None
retorno = None
valores = None

def read_line():
    return input()


retorno = True
valores = read_line().split(" ")
A = int((valores.pop(0)))
B = int((valores.pop(0)))
C = int((valores.pop(0)))
D = int((valores.pop(0)))
if B > C:
  if D > A:
    if D + D > A + B:
      if D >= 0:
        if C >= 0:
          if (A % 2) == 0:
            retorno = False
            print("Valores aceitos")

if retorno:
  print("Valores nao aceitos")