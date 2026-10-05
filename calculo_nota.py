import fucao_nota
print("Programa para calcular média ponderada de um aluno.")
print()

n1=float(input("Insira sua nota: "))
n2=float(input("Insira sua nota: "))
n3=float(input("Insira sua nota: "))

media=fucao_nota.media_ponderada(n1,n2,n3)

print(f"A média das notas é de: {media:.1f}")
