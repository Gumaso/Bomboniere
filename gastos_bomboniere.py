from colorama import Fore, Style


# Importa as bibliotecas colorama para adicionar cores ao terminal

def gastos_equipe():
    print("Coloque o nome do funcionário e quanto ele recebe no dia!")
    funcionarios = {}

    while True:
        while True:
            try:
                # Solicita o nome do funcionário e verifica se é válido
                nome = input("Nome:").title()
                if nome.isspace():
                    raise ValueError("Está vazio")
                for palavra in nome.split():
                    if not palavra.isalpha():
                        raise ValueError("Apenas letras permitidas")
                break
            except ValueError as erro:
                print(f"Erro: {erro}")

        while True:
            try:
                # Solicita o valor a ser pago ao funcionário e verifica se é válido
                diaria = input("Valor a ser pago:")
                if not diaria.isnumeric():
                    raise ValueError("Apenas números e positivos!")
                else:
                    diaria = float(diaria)
                    break
            except ValueError as erro:
                print(f"Erro: {erro}")

        # Atualiza o dicionário de funcionários com o nome e valor da diária
        funcionarios.update({nome: diaria})

        sair = input("Finalizar? [S]/[N]").upper()
        if sair[0] == 'S':
            # Imprime a lista de nomes e valores a serem pagos com formatação de cor
            print(Fore.GREEN + "LISTA DE NOMES E VALORES A SEREM PAGOS" + Style.RESET_ALL)
            print(Fore.GREEN + "_" * 40 + Style.RESET_ALL)
            for nome, valor in funcionarios.items():
                print(f"Nome: {nome} | Valor: R${valor:.2f}")
            break
        else:
            continue
