letras = ["x", "z", "k"]

with open("erros.txt", "w") as arquivo:
    for letra in letras:
        arquivo.write(letra + "\n")
