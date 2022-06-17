# Laboratorio 3.2.1.11
#Luis Daniel Sánchez Cabrera

word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word = input("Ingrese una palabra ")
   # Completa el cuerpo del bucle.
user_word = user_word.upper()
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        word_without_vowels += letter
# Imprimir la palabra asignada a word_without_vowels.
print(word_without_vowels)