#Mateus Henrique Marcimiano Batista

#função recursiva

def Torre_de_Hanoi(n, pino, destino, auxiliar):
    if n == 1:
        print("\n Movendo a peça de", pino, "para", destino)
        return
    Torre_de_Hanoi(n - 1, pino, auxiliar, destino)
    print("\n Movendo a peça de", n, "da torre", pino, "para", destino)
    Torre_de_Hanoi(n - 1, auxiliar, destino, pino)



n = int(input("Digite o número de peças desejadas: "))
Torre_de_Hanoi(n, 'A', 'B', 'C')

result = ((2**n) - 1)

print("\n O número de movimentos realizados foi de:", result)