import random

class Pbm:

    def __init__(self, largura, altura, nomeArquivoSalvo):
        self.largura = largura
        self.altura = altura
        self.nomeArquivoSalvo = nomeArquivoSalvo

    def criaImgPBM(self):
        imgPBM = [[random.choice(['0', '1']) for _ in range(self.largura)] for _ in range(self.altura)]
        return imgPBM
    
    def salvaImgPBM(self):
        with open(self.nomeArquivoSalvo, 'w') as arquivo: 
            arquivo.write('P1\n')
            imgPbm = self.criaImgPBM() 
            arquivo.write(f'{len(imgPbm[0])} {len(imgPbm)}\n') 
            for linha in imgPbm:
                arquivo.write(' '.join(linha) + '\n')