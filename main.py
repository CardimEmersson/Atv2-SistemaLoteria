# Armazena o nome do jogador
playerName = input("Digite o nome do jogador: ")

luckyNumbers = []
while True:
    try:
      for count in range(2):
        luckyNumber = int(input(f"Informe o {count + 1}º numero da sorte entre 0 e 9: "))
        if not 0 <= luckyNumber <= 9:
            raise ValueError("Numero da sorte inválido")
        luckyNumbers.append(luckyNumber)
    except ValueError as e:
        print("Valor inválido: ", e)
    else:
        break

print(playerName)
print(luckyNumbers)