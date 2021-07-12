# NIVELAMENTO DE SENHAS
# Fatores:
#   Mínimo de oito dígitos;
#   Letras maiúsculas e minúsculas;
#   Presença de números;
#   Caracteres especiais;
# Separar em três categorias: Fraca, razoável, forte;
# Fraca: Cumpre no máximo dois fatores.
# Razoável: Cumpre três fatores.
# Forte: Cumpre os quatro fatores.

class Nivelamento_senhas():
    """[Classe fará as ações necessárias para nivelar uma senha]

    Args:
        password ([string]): [senha analizada]
    """
    def __init__(self, password):
        self.password = password
    
    def contagem_caracteres(self): #Dirá se a senha possui mais de oito caracteres
        contagem = 0
        mais_de_oito = False
        for carectere in self.password:
            contagem += 1
        
        if contagem >= 8:
            mais_de_oito = True

        return mais_de_oito
    
    def formato_letra(self): #Dirá se a senha possui caracteres maiúsculos e minúsculos
        maiusculo = False
        minusculo = False
        ambos = False
        for caractere in self.password:
            if caractere.isupper():
                maiusculo = True
            elif caractere.islower():
                minusculo = True
        if maiusculo == True and minusculo == True:
            ambos = True
            return ambos
        return ambos
    
    def existe_numeros(self): # Dirá se a senha possui números
        numero = False
        for carectere in self.password:
            if carectere.isnumeric():
                numero = True
        return numero

    def caracteres_especiais(self): # Dirá se a senha possui caracteres especiais
        especiais = {"!", "@", "#", "$", "%", "&", "*", "?"}
        especial = False
        for caractere in self.password:
            if caractere in especiais:
                especial = True
        return especial
    
    def fraca(self, contagem, formato, numeros, especiais): # Dirá se a senha se enquadra como fraca.
        lista = [contagem, formato, numeros, especiais]
        contagem = 0
        verificacao = True
        for fator in lista:
            if fator == True:
                contagem += 1
        if contagem > 2:
            verificacao = False
        
        return verificacao

    def razoavel(self, contagem, formato, numeros, especiais): # Dirá se a senha se enquadra como razoável.
        lista = [contagem, formato, numeros, especiais]
        contagem = 0
        verificacao = True
        for fator in lista:
            if fator == True:
                contagem += 1
        if contagem < 3 or contagem > 3:
            verificacao = False

        return verificacao

    def forte(self, contagem, formato, numeros, especiais):# Dirá se a senha se enquadra como forte.
        lista = [contagem, formato, numeros, especiais]
        contagem = 0
        verificacao = True
        for fator in lista:
            if fator == True:
                contagem += 1
        if contagem < 4:
            verificacao = False

        return verificacao    

    def verificacao_final(self, fraca, razoavel, forte): #Fará a verificação de fato, retornando a categoria da senha
        resultado = ""
        if fraca == True:
            resultado = resultado + "fraca"
        
        elif razoavel == True:
            resultado = resultado + "razoavel"

        else:
            resultado = resultado + "forte"
        
        return resultado

password = input("Digite sua senha: ")
s1 = Nivelamento_senhas(password)

fraca = s1.fraca(s1.contagem_caracteres(), s1.formato_letra(), s1.existe_numeros(), s1.caracteres_especiais())
razoavel = s1.razoavel(s1.contagem_caracteres(), s1.formato_letra(), s1.existe_numeros(), s1.caracteres_especiais())
forte = s1.forte(s1.contagem_caracteres(), s1.formato_letra(), s1.existe_numeros(), s1.caracteres_especiais())

print(s1.verificacao_final(fraca, razoavel, forte))