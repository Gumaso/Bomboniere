from colorama import Fore, Style


# Importa as bibliotecas colorama para adicionar cores ao terminal

def extras():
    descricao = {}
    print(Fore.GREEN + "-----GASTOS EXTRAS-----" + Style.RESET_ALL)

    while True:
        # Solicita a descrição do gasto extra e o valor correspondente
        nome_gasto = input("Do que se trata o gasto extra?")
        valor = float(input("Qual foi o custo do gasto?"))

        # Atualiza o dicionário de descrição com a descrição do gasto e o valor correspondente
        descricao.update({nome_gasto: valor})

        sair = input("Deseja sair?\n[S]/[N]\n").upper()

        if sair[0] == 'S':
            # Imprime a lista de gastos extras com formatação de cor
            for nome, valor in descricao.items():
                print(f"\033[31m{nome}\033[0m teve o custo de \033[34mR${valor:.2f}\033[0m")
            break
        else:
            continue
