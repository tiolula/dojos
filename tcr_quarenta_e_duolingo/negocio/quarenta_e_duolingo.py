import sys

def verificarPTBR(texto_inserido, resposta_certa):
    return texto_inserido == resposta_certa

def mensagem(resultado):
    if (resultado == True):
        print("Você acertou!")
    else:
        print("Errrrrou!!!!")

if __name__ == "__main__":
    texto_inserido = input("Como se escreve 'quarenta e dois em inglês?\n")
    resultado = verificarPTBR(texto_inserido, "forty two")
    mensagem(resultado)