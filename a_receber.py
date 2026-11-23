def cadastrar_valor(total, quantidade):
    print("\n--- Cadastrar valor ---")

    nome = input("Nome da pessoa que vai pagar: ")
    descricao = input("Descricao do valor: ")
    valor = float(input("Valor a receber: R$ "))

    total = total + valor
    quantidade = quantidade + 1

    print("Valor cadastrado!")
    print(nome, "vai pagar R$", format(valor, ".2f"), "por", descricao)

    return total, quantidade


def mostrar_total(total):
    print("\nTotal a receber: R$", format(total, ".2f"))


def registrar_pagamento(total):
    if total == 0:
        print("Nao existem valores pendentes.")
    else:
        valor_pago = float(input("Digite o valor recebido: R$ "))

        if valor_pago <= total:
            total = total - valor_pago
            print("Pagamento registrado!")
        else:
            print("O valor pago e maior que o total pendente.")

    return total


def mostrar_resumo(quantidade, total):
    print("\n--- Resumo ---")
    print("Quantidade de valores cadastrados:", quantidade)
    print("Total ainda pendente: R$", format(total, ".2f"))


def menu():
    total = 0
    quantidade = 0

    while True:
        print("\n===== A RECEBER =====")
        print("1 - Cadastrar valor")
        print("2 - Mostrar total a receber")
        print("3 - Registrar pagamento")
        print("4 - Mostrar resumo")
        print("0 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            total, quantidade = cadastrar_valor(total, quantidade)
        elif opcao == "2":
            mostrar_total(total)
        elif opcao == "3":
            total = registrar_pagamento(total)
        elif opcao == "4":
            mostrar_resumo(quantidade, total)
        elif opcao == "0":
            print("Programa encerrado.")
            break
        else:
            print("Opcao invalida.")


menu()
