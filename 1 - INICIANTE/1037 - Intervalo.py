numero = None

def aa():
    numero = float(input())
    if numero >= 0:
        if numero <= 25:
            print("Intervalo [0,25]")
        else:
            if numero <= 50:
                print("Intervalo (25,50]")
            else:
                if numero <= 75:
                    print("Intervalo (50,75]")
                else:
                    if numero <= 100:
                        print("Intervalo (75,100]")
                    else:
                        print("Fora de intervalo")
    else:
        print("Fora de intervalo")
