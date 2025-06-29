# formatar o documento para seguir as diretrizes do autopep8, apertar com o direito e selecionar formatar o programa, ou alt+ shif+f8 como atalho
# docbstring, é boa prática, colocar as três aspas logo abaixo da função para explicar o que ela faz, assim, quando for dar manutenção será mais fácil, outra coisa, quando passa o mouse sobre a função diz o que ela faz

def somar(numero1:int, numero2:int):
    """recebe dois numeros inteiros e retorna a soma deles"""
    soma = numero1 + numero2
    return soma


def subtrair(numero1, numero2):
    subtrai = numero1 - numero2
    return subtrai


def multiplicar(numero1, numero2):
    multiplica = numero1 * numero2
    return multiplica


def dividir(numero1, numero2):
    if numero2 == 0:
        return "Erro! Não é possível dividir por zero."
    dividi = numero1 / numero2
    return dividi


def exibir_menu():
    print("Seja bem vindo a calculadora do Rafa! Quer fazer o que?")
    print("1 - Somar ")
    print("2 - Subtrair ")
    print("3 - Multiplicar ")
    print("4 - Dividir ")
    print("5 - Já quer sair ? ")


# Função para realizar as operações conforme a escolha do usuário
def calculadora():
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção (1-5): ")

        if escolha == "5":
            print("Saindo... Até logo!")
            break

        try:
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, digite números válidos.")
            continue

        if escolha == "1":
            resultado = somar(numero1, numero2)
            print(f"O resultado da soma é: {resultado}")
        elif escolha == "2":
            resultado = subtrair(numero1, numero2)
            print(f"O resultado da subtração é: {resultado}")
        elif escolha == "3":
            resultado = multiplicar(numero1, numero2)
            print(f"O resultado da multiplicação é: {resultado}")
        elif escolha == "4":
            resultado = dividir(numero1, numero2)
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")


# Inicia a calculadora
if __name__ == "__main__":
    calculadora()
