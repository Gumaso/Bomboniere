from colorama import Fore, Back, Style
# Imprime a descrição da Bomboniere com formatação de cor
print(Fore.GREEN + ("_" * 10) + "Descrição Bomboniere" + ("_" * 10) + Style.RESET_ALL)

# Dicionário de produtos e preços
produtos = {"Chiclete": 2, "Trufas": 0.2, "Pirulitos": 5, "Açai": 4, "Paçoca": 2.5, "Dadinho de Caramelo": 3.2}

# Imprime os nomes dos itens e seus respectivos preços
for item in produtos.items():
    print(f"{item[0]}: R${item[1]}")

# Imprime a seção "COMPRANDO" com formatação de cor
print(Fore.GREEN + ("_" * 10) + "COMPRANDO" + ("_" * 10) + Style.RESET_ALL)

# Pergunta ao usuário se deseja efetuar uma compra
comprar = input("Deseja efetuar uma compra? [S]/[N]").upper()

if comprar[0] == "S":
    while True:
        total = 0
        compras = []

        # Solicita a quantidade de cada item a ser comprado
        for item in produtos.items():
            compra = int(input(f"Quantas unidades de: {item[0]}\n"
                               f"Custa R${item[1]:.2f} a unidade!\nQuantidade:"))
            print(Fore.RED + ("_" * 5) + "ADICIONADO AO CARRINHO" + ("_" * 5) + Style.RESET_ALL)

            compra = int(compra)
            calculo = compra * item[1]
            total += calculo
            msg = f"{compra} unidade(s) de {item[0]} por R${item[1]:.2f} é igual a: R${calculo:.2f}"
            compras.append(msg)

        # Imprime as mensagens de confirmação das compras
        for mensagem in compras:
            print(mensagem)

        # Imprime o total gasto
        print(f"Total gasto: R${total:.2f}")
        break
else:
    print("Nenhuma compra efetuada, ganho total R$00,00")


