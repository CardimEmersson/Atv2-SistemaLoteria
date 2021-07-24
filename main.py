game = []

while True:
    try:

        playerName = input("Digite o nome do jogador: ")
        luckyNumbers = []

        for count in range(2):
            luckyNumber = int(
                input(f"Informe o {count + 1}º numero da sorte entre 0 e 9: "))
            if not 0 <= luckyNumber <= 9:
                raise ValueError("Numero da sorte inválido")
            luckyNumbers.append(luckyNumber)

        game.append([playerName, luckyNumbers])

        newGame = input("Adicionar novo jogo? sim ou nao: ")
        if newGame != "sim":
            break
    except ValueError as e:
        print("Valor inválido: ", e)

print(game)
