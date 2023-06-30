from colorama import Fore, Back, Style

print(Fore.GREEN + ("_" * 10) + "Descrição Bomboniere" + ("_" * 10) + Style.RESET_ALL)

produtos = {"Chiclete": 2, "Trufas": 0.2, "Pirulitos": 5,
            "Açai": 4, "Paçoca": 2.5, "Dadinho de Caramelo": 3.2}
for itens in produtos.items():
    print(f"{itens[0]}: R${itens[1]}")
