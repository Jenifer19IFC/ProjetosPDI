import random

class Ppm:

    def __init__(self, largura, altura, intensidadeMax, nomeArquivoSalvo):
        self.largura = largura
        self.altura = altura
        self.intensidadeMax = intensidadeMax
        self.nomeArquivoSalvo = nomeArquivoSalvo

    def criaImgPPM(self):
        imgPPM = [
            [(str(random.randint(0, self.intensidadeMax)), str(random.randint(0, self.intensidadeMax)), str(random.randint(0, self.intensidadeMax)))
                for _ in range(self.largura)
            ]
            for _ in range(self.altura)
        ]
        return imgPPM
        
    def salvaImgPPM(self):
        with open(self.nomeArquivoSalvo, 'w') as arquivo:
            arquivo.write('P3\n')
            imgPpm = self.criaImgPPM()
            arquivo.write(f'{len(imgPpm[0])} {len(imgPpm)} {self.intensidadeMax}\n')
            for linha in imgPpm:
                arquivo.write(' '.join(' '.join(pixel) for pixel in linha) + '\n')