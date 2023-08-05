import random

def criaImgPBM(largura, altura):
    imgPBM = [[random.choice(['0', '1']) for _ in range(largura)] for _ in range(altura)]
    return imgPBM

def criaImgPGM(largura, altura, intensidadeMax):
    imgPGM = [[str(random.randint(0, intensidadeMax)) for _ in range(largura)] for _ in range(altura)]
    return imgPGM

def salvar_imgPBM(nomeArquivo, imgPBM):
    with open(nomeArquivo, 'w') as arquivo: 
        arquivo.write('P1\n') 
        arquivo.write(f'{len(imgPBM[0])} {len(imgPBM)}\n') 
        for linha in imgPBM:
            arquivo.write(' '.join(linha) + '\n')

def salvar_imgPGM(nomeArquivo, imgPGM, intensidadeMax):
    with open(nomeArquivo, 'w') as arquivo: # Abre arquivo no modo escrita ('w')
        arquivo.write('P2\n') # Escreve cabeçalho o tipo da img
        arquivo.write(f'{len(imgPGM[0])} {len(imgPGM)}\n') # Escreve largura altura (Ex: 400 400)
        arquivo.write(f'{intensidadeMax}\n') # Escreve intensidade máxima de cada pixel
        for linha in imgPGM: 
            arquivo.write(' '.join(linha) + '\n') # Uni elementos separando por espaço
            # A cada linha há uma quebra de linha

# Tamanho da imagem
largura, altura = 400, 400

# Nível máximo de intensidade de cinza (PGM)
intensidadeMax = 15  # 16 níveis de 0 a 15 (4 bits)

# Cria img PBM
imgPBM = criaImgPBM(largura, altura)
# Salva imagem PBM
salvar_imgPBM('imgPretoBranco.pbm', imgPBM)

# Cria img PGM
imgPGM = criaImgPGM(largura, altura, intensidadeMax)
# Salva img PGM
salvar_imgPGM('imgTonsCinza.pgm', imgPGM, intensidadeMax)