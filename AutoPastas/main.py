import datetime
from arquivo import Arquivo
from pasta import Pasta

diretorio_raiz = 'C:\\Users\\1572173\\source\\LEONAN\\Arquivos\\'
a = datetime.datetime.now().strftime('%d%m%Y')
b = datetime.datetime.now().strftime('%M%S%f')
diretorio = diretorio_raiz +a +'\\'
nome = 'file_' + b + '.txt'
pasta = Pasta(diretorio)
texto = ['Ola','teste','de','criacao','leitura','gravação']

pasta.arrumarPastas('_')
#pasta.criar()
pasta.deletar()
'''for x in range(1,5001):
    b = datetime.datetime.now().strftime('%M%S%f')
    nome = str(x)+'file_' + b + '.txt'
    arquivo = Arquivo(nome, diretorio)
    arquivo.criar()'''