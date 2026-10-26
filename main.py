import csv


def abrir_estoque():
    try:
        with open("estoque_mercado.csv", "r", encoding="utf-8") as arquivo:
            print("Estoque aberto 📦")
            print(arquivo.read())
    except FileNotFoundError:
        print("O arquivo estoque_mercado.csv não foi encontrado.")


def verificar_estoque():
    print("Conferindo estoque 🔃")


def somar_quantidades():
    total = 0

    try:
        with open("estoque_mercado.csv", "r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)
            if leitor.fieldnames is None or "quantidade" not in leitor.fieldnames:
                print("A coluna 'quantidade' não foi encontrada no arquivo.")
                return

            for numero_linha, linha in enumerate(leitor, start=2):
                try:
                    total += int(linha["quantidade"])
                except (TypeError, ValueError):
                    print(f"Quantidade inválida na linha {numero_linha}.")
                    return

        print(f"Quantidade total em estoque: {total}")
    except FileNotFoundError:
        print("O arquivo estoque_mercado.csv não foi encontrado.")


def fechar_estoque():
    print("Estoque encerrado 🔒")


def menu():
    while True:
        print("\n=== Mercado ===")
        print("1 - Abrir o estoque")
        print("2 - Conferir o estoque")
        print("3 - Somar quantidades")
        print("4 - Encerrar")

        opcao = input("Selecione uma opção: ").strip()

        if opcao == "1":
            abrir_estoque()
        elif opcao == "2":
            verificar_estoque()
        elif opcao == "3":
            somar_quantidades()
        elif opcao == "4":
            fechar_estoque()
            break
        else:
            print("Opção inválida.")


menu()
