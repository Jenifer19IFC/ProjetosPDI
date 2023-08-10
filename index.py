from CriaImagens.ClassPbm import Pbm
from CriaImagens.ClassPgm import Pgm
from CriaImagens.ClassPpm import Ppm

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