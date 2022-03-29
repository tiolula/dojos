import sys

def verificarPTBR(texto_inserido, resposta_certa):
    return texto_inserido == resposta_certa

def mensagem(resultado):
    if (resultado == True):
        print("Você acertou!")
    else:
        print("Errrrrou!!!!")

if __name__ == "__main__":
    palavra = "quarenta e dois"
    resposta_certa = "forty two"
    texto_inserido = input("Como se escreve " + palavra + " em inglês?\n")
    resultado = verificarPTBR(texto_inserido, resposta_certa)
    mensagem(resultado)