lista_animais = ['macaco', 'tigre', 'onça', 'crocodilo', 'tartaruga']

with open("animais.txt", "w") as animais:
    for i in lista_animais:
        animais.write(f"{i}\n")