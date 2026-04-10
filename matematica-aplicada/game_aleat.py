import random

max_n = 100
numero_secreto = random.randint(1, max_n)
tentativas = 0
acertou = False

print(numero_secreto)
print("Bem-vindo ao jogo Adivinhe o Número!")
print(f"Tente adivinhar o número entre 1 e {max_n}.")
print("Para finalizar o jogo digite 0")

while not acertou:
    palpite = int(input("Digite seu palpite: "))

    if palpite == 0:
        print(f"Jogo finalizado antecipadamente.")
        print("========== FIM DE JOGO ==========")
        break
    tentativas += 1
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        print("=================== FIM DE JOGO ===================")
        acertou = True
    elif palpite < 0 or palpite > max_n:
        print("Numero fora do intervalo considerado, jogada ruim.")
    elif palpite < numero_secreto:
        print("Palpite MENOR que o numero secreto")
    else:
        print("Palpite MAIOR que o numero secreto")