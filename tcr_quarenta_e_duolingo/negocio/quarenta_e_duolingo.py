def verificarPTBR(palavra_para_traducao, palavra_que_vai_ser_traduzida):
    return palavra_para_traducao == palavra_que_vai_ser_traduzida

def mensagem(resultado):
    if (resultado == True):
        print("Você acertou!")
    print("Errrrrou!!!!")