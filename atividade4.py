letras = ["x", "z", "k"]
# Escreve cada letra em uma linha no arquivo erros.txt
with open("erros.txt", "w") as arquivo:
    for letra in letras:
        arquivo.write(letra + "\n")