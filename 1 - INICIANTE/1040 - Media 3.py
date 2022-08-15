#https://www.beecrowd.com.br/judge/pt/problems/view/1040

while True:
    try:
        n1, n2, n3, n4 = list(map(float, input().split()))
    except:
        break
    media = (n1*2+n2*3+n3*4+n4*1)/10
    exame = False
    print(f"Media: {(media):.1f}")

    if 5.0 <= media < 7.0:
        print("Aluno em exame.")
        exame = float(input())
        print(f"Nota do exame: {exame:.1f}")
        media = (exame + media) / 2

    if media < 5.0:
        print("Aluno reprovado.")
        continue
    else:
        print("Aluno aprovado.")

    if exame:
        print(f"Media final: {media:.1f}")
