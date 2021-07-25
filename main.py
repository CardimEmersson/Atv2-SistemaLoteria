import random

games = []

while True:
    try:
        playerName = input("Digite o nome do jogador: ")
        if not playerName.strip():
            raise ValueError("Nome inválido")
        luckyNumbers = []

        for count in range(2):
            luckyNumber = int(
                input(
                    f"Informe seu {count + 1}º numero da sorte entre 0 e 9: "))
            if not 0 <= luckyNumber <= 9:
                raise ValueError("Numero da sorte inválido")
            luckyNumbers.append(luckyNumber)

        games.append([playerName, luckyNumbers])

        newGame = input("Adicionar novo jogo? sim ou nao: ")
        if newGame != "sim":
            break
    except ValueError as e:
        print("Valor inválido: ", e)

drawnNumbers = []
drawnNumbers.append(int(random.random() * 2))
drawnNumbers.append(int(random.random() * 2))

print("numeros sorteados: ", drawnNumbers)

drawnPlayers = []
for game in games:
    intersection = list(set(drawnNumbers) & set(game[1]))
    if len(intersection) == 2:
        drawnPlayers.append(game[0])

if (drawnPlayers):
    for drawnPlayer in drawnPlayers:
        print("Jogador sorteado: ", drawnPlayer)
else:
    print("Nenhum jogador sorteado!")