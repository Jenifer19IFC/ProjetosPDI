import random

class Pgm:

    def __init__(self, largura, altura, intensidadeMax, nomeArquivoSalvo):
        self.largura = largura
        self.altura = altura
        self.intensidadeMax = intensidadeMax
        self.nomeArquivoSalvo = nomeArquivoSalvo

    def criaImgPGM(self):
        imgPGM = [[str(random.randint(0, self.intensidadeMax)) for _ in range(self.largura)] for _ in range(self.altura)]
        return imgPGM
    
    def salvaImgPGM(self):
        with open(self.nomeArquivoSalvo, 'w') as arquivo: # Abre arquivo no modo escrita ('w')
            arquivo.write('P2\n') # Escreve cabeçalho o tipo da img
            imgPgm = self.criaImgPGM()
            arquivo.write(f'{len(imgPgm[0])} {len(imgPgm)}\n') # Escreve largura altura (Ex: 400 400)
            arquivo.write(f'{self.intensidadeMax}\n') # Escreve intensidade máxima de cada pixel
            for linha in imgPgm: 
                arquivo.write(' '.join(linha) + '\n') # Uni elementos separando por espaço
                # A cada linha há uma quebra de linha