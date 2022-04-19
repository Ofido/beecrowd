#https://www.beecrowd.com.br/judge/pt/problems/view/1168
#

for _ in range(int(input())):
    numeros = input()
    leds = 0
    for algarismo in numeros:
        if algarismo == "1":
            leds += 2
            continue
        if algarismo in ["2", "3", "5"]:
            leds += 5
            continue
        if algarismo == "4":
            leds += 4
            continue
        if algarismo in ["6", "9", "0"]:
            leds += 6
            continue
        if algarismo == "7":
            leds += 3
            continue
        if algarismo == "8":
            leds += 7
            
    print(f"{leds} leds")
