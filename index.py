from CriaImagens.ClassPbm import Pbm
from CriaImagens.ClassPgm import Pgm
from CriaImagens.ClassPpm import Ppm
from RedimensionarResolucao.ClassRedimensionarPgm import RedimensionarPgm

# --------------- PBM - Preto e Branco --------------------
# Tamanho da imagem
largura, altura = 400, 400

# Cria img PBM
imgPBM = Pbm(largura, altura,'imgPretoBranco.pbm')
imgPBM.salvaImgPBM()


# --------------- PGM - Tons de Cinza --------------------

# Nível máximo de intensidade de cinza (PGM)
intensidadeMax = 15  # 16 níveis de 0 a 15 (4 bits)

imgPGM = Pgm(largura, altura, intensidadeMax, 'imgTonsCinza.pgm')
imgPGM.salvaImgPGM()


# --------------- PPM - Colorido --------------------

imgPPM = Ppm(largura, altura, intensidadeMax, 'imgColorida.ppm')
imgPPM.salvaImgPPM()

# --------------- Redimensionar resolução de imagem --------------------


# Caminho para o arquivo PGM de entrada e saída
caminhoArquivoEntrada = "teste.pgm"
caminhoArquivoSaída = "imagem_redimensionada.pgm"

# Define a nova largura e altura
novaLargura = 8
novaAltura = 8

redimensionador = RedimensionarPgm()
redimensionador.redimensionarImagem(caminhoArquivoEntrada, caminhoArquivoSaída, novaLargura, novaAltura)
