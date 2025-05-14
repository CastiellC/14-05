
with open("animais.txt", "r") as animais:
 lista_animais= animais.read().splitlines()

for i in lista_animais:
    print(f"animal : {i}") 