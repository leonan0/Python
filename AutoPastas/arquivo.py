from Lib import os, shutil

class Arquivo():

    def __init__(self, nome, diretorio):
        self.nome = nome
        self.diretorio = diretorio
<<<<<<< HEAD
        self.path = diretorio+nome

    def criar(self):
        try:
            arquivo = open(self.path, 'a')
            arquivo.close()
            return arquivo
=======
    
    def criar(self):
        try:
            arquivo = open(self.diretorio+self.nome, 'w')
>>>>>>> 474f3bdeaafbf4c21ccf05b07c613f9c4b06fd67
        except:
            pass

    def editar(self, nome_novo):
        try:
<<<<<<< HEAD
            arquivo = os.rename(self.path, self.diretorio+nome_novo)
            self.nome = nome_novo
            self.path = self.diretorio+nome_novo
=======
            arquivo = os.rename(self.diretorio+self.nome, self.diretorio+nome_novo)
            self.nome = nome_novo
>>>>>>> 474f3bdeaafbf4c21ccf05b07c613f9c4b06fd67
        except:
            pass

    def deletar(self):
        try:
<<<<<<< HEAD
            arquivo = os.remove(self.path)
=======
            arquivo = os.remove(self.diretorio+self.nome)
>>>>>>> 474f3bdeaafbf4c21ccf05b07c613f9c4b06fd67
        except:
            pass

    def mover(self, novo_diretorio):
        try:
<<<<<<< HEAD
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
=======
            arquivo = shutil.move(self.diretorio+self.nome, novo_diretorio)
            self.diretorio = novo_diretorio
        except:
            pass


>>>>>>> 474f3bdeaafbf4c21ccf05b07c613f9c4b06fd67

