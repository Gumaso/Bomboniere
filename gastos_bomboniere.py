def gastos_equipe():
    print("Coloque o nome do funcionário e quanto ele recebe no dia!")
    funcionarios = {}
    while True:
        while True:
            try:
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
                diaria = input("Valor á ser pago:")
                if not diaria.isnumeric():
                    raise ValueError("Apenas números e positivos!")
                else:
                    diaria = float(diaria)
                    break
            except ValueError as erro:
                print(f"Erro:{erro}")
        funcionarios.update({nome: diaria})
        sair = input("Finalizar?[S]/[N]").upper()
        if sair[0] == 'S':
            print("LISTA DE NOMES E VALORES A SEREM PAGOS")
            print("_"*20)
            for n, v in funcionarios.items():
                print(f"Nome: {n} | Valor: R${v:.2f}")
            break
        else:
            continue
