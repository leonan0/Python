from Lib import os, shutil

class Arquivo():

    def __init__(self, nome, diretorio):
        self.nome = nome
        self.diretorio = diretorio
    
    def criar(self):
        try:
            arquivo = open(self.diretorio+self.nome, 'w')
        except:
            pass

    def editar(self, nome_novo):
        try:
            arquivo = os.rename(self.diretorio+self.nome, self.diretorio+nome_novo)
            self.nome = nome_novo
        except:
            pass

    def deletar(self):
        try:
            arquivo = os.remove(self.diretorio+self.nome)
        except:
            pass

    def mover(self, novo_diretorio):
        try:
            arquivo = shutil.move(self.diretorio+self.nome, novo_diretorio)
            self.diretorio = novo_diretorio
        except:
            pass



