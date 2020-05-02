import random as rand
import datetime
from arquivo import Arquivo
from pasta import Pasta

#diretorio_raiz = 'C:\\Users\\1572173\\source\\LEONAN\\Arquivos\\'
diretorio_raiz = 'D:\\Usuario\\Source\\Arquivos\\'
a = datetime.datetime.now().strftime('%d%m%Y')
b = datetime.datetime.now().strftime('%M%S%f')
c = datetime.datetime.now().strftime('%Y_%m_%d_%M_%S_%f')
diretorio = diretorio_raiz +a +'\\'
nome = 'file_' + c + '.txt'
pasta = Pasta(diretorio)
pasta.criar()

#pasta.deletar(diretorio_raiz)
#pasta.arrumarPastas('_', [2,5,0,7])

# for x in range(1,5001):
#     b = datetime.datetime.now().strftime('%Y_%m_%d_%M_%S_%f')
#     h = rand.randrange(50)
#     nome_ = str(h) + '_file_' + b + '.txt' 
#     arquivo = Arquivo(nome_, diretorio)
#     arquivo.criar()