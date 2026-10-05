print("Programa para calcular média ponderada de um aluno.")
print()

n1=float(input("Insira sua nota: "))
n2=float(input("Insira sua nota: "))
n3=float(input("Insira sua nota: "))

p1=2
p2=3
p3=5

if n1>p1 or n2>p2 or n3>p3:
    print("Nota invalida")
    exit()

media=(n1*p1+n2*p2+n3*p3)/(p1+p2+p3)

print(f"A média das notas é de: {media:.1f}")
