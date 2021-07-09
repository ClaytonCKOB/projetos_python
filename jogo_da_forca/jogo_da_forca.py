from words_in_portuguese import words
import random
import string

#JOGO DA FORCA
# Programa simples com 

def escolher_palavra(words): #Pega alguma palavra aleatoriamente dentro das especificações
    word = random.choice(words)
    word = word.upper() #Padroniza todas as strings em uppercase
    caracteres_invalidos = {"Á"}
    while "Á" or "Ã" or "Â" or "É" or "Ẽ" or "Ê" in word:#Retira as palavras com caracteres especiais
        word = random.choice(words)
        word = word.upper()
    return word

def jogar():#Função principal do jogo
    word = escolher_palavra(words)
    letters_in_word = set(word)
    letras_usadas = set()
    alfabeto = set(string.ascii_uppercase)
    vidas = 5

    while len(letters_in_word) > 0 and vidas != 0:
        print("--------------------//--------------------\n")
        print("Você tem " + str(vidas) + " vidas.\n")
        print("Você já utilizou estas letras: " + " ".join(letras_usadas) + "\n")
        lista_de_palavras = ""
        for letter in word:
            if letter in letras_usadas:
                lista_de_palavras += letter
            else:
                lista_de_palavras += "-"
        print("Sua palavra é " + lista_de_palavras + "\n")

        letra_user = input("Digite uma letra: ").upper()
        if letra_user in alfabeto and letra_user not in letras_usadas:
            letras_usadas.add(letra_user)
            if letra_user in letters_in_word:
                letters_in_word.remove(letra_user)
            else:
                vidas = vidas - 1
        elif letra_user in letras_usadas:
            print("Você já digitou esta letra.")
        else:
            print("Digite um valor correto!")
    if vidas == 0:
        print("Você perdeu, tente novamente.")
    else:
        print("Parabéns, você acertou! A palavra era " + word)

jogar()