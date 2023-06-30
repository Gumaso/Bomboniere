def extras():
    descricao = {}
    while True:
        nome_gasto = input("Do que se trata o gasto extra?")
        valor = float(input("Qual foi o custo do gasto?"))
        descricao.update({nome_gasto: valor})
        sair = input("Deseja sair?\n[S]/[N]\n").upper()
        if sair[0] == 'S':
            for n, v in descricao.items():
                print(f"\033[31m{n}\033[0m teve o custo de \033[34mR${v:.2f}\033[0m")
            break
        else:
            continue
