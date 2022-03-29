import sys

def verificarPTBR(palavra_para_traducao, palavra_que_vai_ser_traduzida):
    return palavra_para_traducao == palavra_que_vai_ser_traduzida

def mensagem(resultado):
    if (resultado == True):
        print("Você acertou!")
    else:
        print("Errrrrou!!!!")

if __name__ == "__main__":
    texto_inserido = input("Como se escreve 'quarenta e dois em inglês?\n")