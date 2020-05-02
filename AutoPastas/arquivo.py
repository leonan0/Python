from Lib import os, shutil
import pasta as Pasta

class Arquivo():

    def __init__(self, nome, diretorio):
        self.nome = nome
        self.diretorio = diretorio
        self.path = diretorio+nome

    def criar(self):
        try:
            arquivo = open(self.path, 'a')
            arquivo.close()
            return arquivo
        except:
            pass

    def editar(self, nome_novo):
        try:
            arquivo = os.rename(self.path, self.diretorio+nome_novo)
            self.nome = nome_novo
            self.path = self.diretorio+nome_novo
        except:
            pass

    def deletar(self):
        try:
            arquivo = os.remove(self.path)
        except:
            pass

    def mover(self, novo_diretorio):
        try:
            arquivo = shutil.move(self.path, novo_diretorio+self.nome)
            self.diretorio = novo_diretorio
            self.path = novo_diretorio+self.nome
        except:
            pass

    def ler(self):
            self.criar()
            arquivo = open(self.path)
            linhas = arquivo.readlines()

    def escrever(self,texto):
        self.criar()
        arquivo = open(self.path, 'a')
        count = 0
        for linha in texto:
            if count > 0:
                arquivo.write('\n'+linha)
            else:
                arquivo.write(linha)
            count =+ 1

    def listarArquivos(self):
        pasta = Pasta(self.diretorio)
        lista = pasta.listar()
        arquivos = []
        for a in lista:
            a = self.diretorio+a
            if os.path.isfile(a):
                arquivos.append(a)
            else:
                continue
        return arquivos
        

    def arrumaArquivos(self, separador, item=0):
        pasta = Pasta(self.diretorio)
        pass

