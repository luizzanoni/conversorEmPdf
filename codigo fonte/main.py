# conversor de qualquer extensão para PDF
# Powered by: Luiz Gustavo Zanoni
# Date 16/08/2022
# Chapecó - Brasil

import os
import time
start = time.time()
print("Programa iniciado, aguarde o término em SEGUNDOS.")
from PIL import Image # pip install pillow

for file in os.listdir():
    if file.split('.')[-1] in ('tif', 'tiff', 'DWTIFF', 'DWTiff', 'png', 'jpg', 'jpeg', 'gif', 'bmp', 'psd', 'png', 'fgv', 'raw', 'webp', 'svg'):
        file_name = os.path.basename(file).split('.')[-2]
        imagem = Image.open(file)
        imagem_convertida = imagem.convert('RGB')
        imagem_convertida.save('{0}.pdf'.format(file_name))
end = time.time()
print(end - start)
