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
caminhoArquivoEntrada = "RedimensionarResolucao/entrada.pgm"

# Define a nova largura e altura
novaLargura = 400 
novaAltura = 400

redimensionador = RedimensionarPgm()
redimensionador.redimensionarImagemGenerico(caminhoArquivoEntrada, novaLargura, novaAltura)
redimensionador.redimensionarImgDezVezesMenor(caminhoArquivoEntrada)
redimensionador.redimensionarImgTamPadrao(caminhoArquivoEntrada)
redimensionador.redimensionarImgHD720p(caminhoArquivoEntrada)
redimensionador.redimensionarImgFullHd1080p(caminhoArquivoEntrada)
redimensionador.redimensionarImg4k(caminhoArquivoEntrada)
redimensionador.redimensionarImg8k(caminhoArquivoEntrada)




