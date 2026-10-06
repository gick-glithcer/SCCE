def abrir_estoque():
    try:
        with open("estoque_mercado.csv", "r", encoding="utf-8") as arquivo:
            print("Estoque aberto 📦")
            print(arquivo.read())
    except FileNotFoundError:
        print("O arquivo estoque_mercado.csv não foi encontrado.")


def verificar_estoque():
    print("Conferindo estoque 🔃")


def fechar_estoque():
    print("Estoque encerrado 🔒")


def menu():
    while True:
        print("\n=== Mercado ===")
        print("1 - Abrir o estoque")
        print("2 - Conferir o estoque")
        print("3 - Encerrar")

        opcao = input("Selecione uma opção: ").strip()

        if opcao == "1":
            abrir_estoque()
        elif opcao == "2":
            verificar_estoque()
        elif opcao == "3":
            fechar_estoque()
            break
        else:
            print("Opção inválida.")


menu()
