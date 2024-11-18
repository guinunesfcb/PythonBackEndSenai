import random

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número entre 1 e 100. Você tem 10 tentativas.")

numeroAleatorio = random.randint(1, 100)
tentativas = 10

for tentativa in range(1, tentativas + 1):
    print(f"Tentativa: {tentativa}/{tentativas}")
    adivinharNumero = int(input("Digite um número: "))

    if adivinharNumero == numeroAleatorio:
        print(
            f"👏 Você acertou o número sorteado: {numeroAleatorio}! Parabéns 👏")
        break
    elif adivinharNumero < numeroAleatorio:
        print("O número é maior! Tente novamente.")
    else:
        print("O número é menor! Tente novamente.")
else:
    print(
        f"😢 Você usou todas as tentativas. O número era {numeroAleatorio}. Boa sorte na próxima!")
