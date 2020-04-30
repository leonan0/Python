import datetime
from arquivo import Arquivo
from pasta import Pasta

diretorio_raiz = 'D:\\Usuario\\Desktop\\Teste\\'
a = datetime.datetime.now().strftime('%d%m%Y')
b = datetime.datetime.now().strftime('%M%S%f')
diretorio = diretorio_raiz + a +'\\'
nome = 'file_' + b + '.txt'
pasta = Pasta(diretorio)
arquivo = Arquivo(nome, diretorio)

pasta.criar()
arquivo.criar()
pasta.deletar()


