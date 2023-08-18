class RedimensionarPgm:

    def getInfArquivoPgm(self, caminhoArquivo):
        with open(caminhoArquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        tipo = linhas[0].strip()  # P2
        largura, altura = map(int, linhas[1].split())  # Ex: 800x800
        intensidadeMax = int(linhas[2])  
        listPixels = list(map(int, ' '.join(linhas[3:]).split()))  # Lista de valores de pixels

        return largura, altura, intensidadeMax, listPixels

    def interpolaVizinhoMaisProximo(self, larguraOriginal, alturaOriginal, pixelsOriginais, novaLargura, novaAltura):
        escalaX = larguraOriginal / novaLargura  # Fator de escala na direção X
        escalaY = alturaOriginal / novaAltura  # Fator de escala na direção Y

        novaImg = []

        for y in range(novaAltura):
            for x in range(novaLargura):
                xOriginal = int(x * escalaX)  # Calcula a coordenada X original correspondente
                yOriginal = int(y * escalaY)  # Calcula a coordenada Y original correspondente
                indiceOriginal = yOriginal * larguraOriginal + xOriginal  # Calcula o índice do pixel original
                novaImg.append(pixelsOriginais[indiceOriginal])  # Adiciona o valor do pixel à nova imagem

        return novaImg

    def escreveArquivoPgm(self, caminhoArquivoSaída, novaLargura, novaAltura, intensidadeMax, novaImg):
        with open(caminhoArquivoSaída, 'w') as arquivo:
            arquivo.write("P2\n")  
            arquivo.write(f"{novaLargura} {novaAltura}\n")  
            arquivo.write(f"{intensidadeMax}\n")  

            for i in range(novaAltura):
                for j in range(novaLargura):
                    valor = novaImg[i * novaLargura + j]  # Obtém o valor do pixel da nova img
                    arquivo.write(str(valor))  # Valor do pixel
                    arquivo.write(" ")  

                arquivo.write("\n")  

    def redimensionarImagem(self, caminhoArquivoEntrada, caminhoArquivoSaída, novaLargura, novaAltura):
        larguraOriginal, alturaOriginal, intensidadeMax, pixelsOriginais = self.getInfArquivoPgm(caminhoArquivoEntrada)
        novaImg = self.interpolaVizinhoMaisProximo(larguraOriginal, alturaOriginal, pixelsOriginais, novaLargura, novaAltura) 
        self.escreveArquivoPgm(caminhoArquivoSaída, novaLargura, novaAltura, intensidadeMax, novaImg)
        print("Arquivo PGM redimensionado gerado com sucesso!\nCaminho: ", caminhoArquivoSaída)
