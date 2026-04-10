def criar_tabuleiro():
    return [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

def mostrar_tabuleiro(tabuleiro):
    print("\n 0 1 2")
    print(" -------------")
    for i in range(3):
        print(f"{i} | {tabuleiro[i][0]} | {tabuleiro[i][1]} | {tabuleiro[i][2]} |")
        print(" -------------")

def jogada_valida(tabuleiro, linha, coluna):
    if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
        return False
    if tabuleiro[linha][coluna] != " ":
        return False
    return True

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for i in range(3):
        if tabuleiro[i][0] == jogador and tabuleiro[i][1] == jogador and tabuleiro[i][2] == jogador:
            return True
    # Verificar colunas
    for j in range(3):
        if tabuleiro[0][j] == jogador and tabuleiro[1][j] == jogador and tabuleiro[2][j] == jogador:
            return True
    # Verificar diagonal principal
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    # Verificar diagonal secundária
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

def verificar_empate(tabuleiro):
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == " ":
                return False
    return True

def alternar_jogador(jogador_atual):
    if jogador_atual == "X":
        return "O"
    else:
        return "X"

def jogar():
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"
    print("=== JOGO DA VELHA ===")
    print("Os jogadores devem informar linha e coluna.")
    print("As posições vão de 0 até 2.")
    while True:
        mostrar_tabuleiro(tabuleiro)
        print(f"\nJogador {jogador_atual}, é a sua vez.")
        linha = int(input("Digite a linha: "))
        coluna = int(input("Digite a coluna: "))
        # if linha==5 and coluna==5:
        #     print("Jogo finalizado antecipadamente")
        #     break
        if not jogada_valida(tabuleiro, linha, coluna):
            print("\nJogada inválida. Tente novamente.")
            continue
        tabuleiro[linha][coluna] = jogador_atual
        if verificar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"\nParabéns! O jogador {jogador_atual} venceu!")
            break
        if verificar_empate(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print("\nO jogo terminou em empate!")
            break
        jogador_atual = alternar_jogador(jogador_atual)

jogar()