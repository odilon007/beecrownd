import os

target_dir = "python"

while True:
    num = input("\nNúmero do problema (ou ENTER para sair): ").strip()
    if num == "":
        print("Encerrado.")
        break

    print("Cole o código abaixo. Termine com uma linha contendo apenas 'EOF':")

    linhas = []
    while True:
        linha = input()
        if linha == "EOF":
            break
        linhas.append(linha)

    filename = f"{num}.cpp"
    filepath = os.path.join(target_dir, filename)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))

    print(f"Arquivo salvo: {filepath}")
