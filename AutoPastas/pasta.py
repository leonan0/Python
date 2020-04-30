<<<<<<< HEAD
from Lib import os,shutil
from arquivo import Arquivo
=======
from Lib import os
>>>>>>> 474f3bdeaafbf4c21ccf05b07c613f9c4b06fd67

class Pasta():

    def __init__(self, caminho):
        self.caminho = caminho
        self.existe = self.situacao()

    def criar(self):
        try:
            if self.existe == False:
<<<<<<< HEAD
                os.makedirs(self.caminho)
=======
                pasta = os.makedirs(self.caminho)
>>>>>>> 474f3bdeaafbf4c21ccf05b07c613f9c4b06fd67
                self.existe = True
            else:
                pass
        except:
            pass

    def editar(self, novo_caminho):
        try:
            pasta = os.rename(self.caminho, novo_caminho)
            self.caminho = novo_caminho
        except:
            pass

<<<<<<< HEAD
    def deletar(self,caminho=False):
            shutil.rmtree(self.caminho)

    def situacao(self):
        try:
            if os.path.exists(self.caminho):
                return True
            else:
                return False
        except:
            pass

    def listar(self,caminho=True):
        if caminho == True:
            lista = os.listdir(self.caminho)
        else:
            lista = os.listdir(caminho)
        return lista

    def arrumarPastas(self,separador):
        pastas = self.listar()
        for pasta in pastas:
            if '.txt' in pasta:
                arquivo = Arquivo(pasta,self.caminho)
                caminho_ = arquivo.diretorio+pasta.split(separador)[1].replace('.txt', '')+'\\'
                pastax = Pasta(caminho_)
                pastax.criar()
                arquivo.mover(caminho_)
            else:
                continue



=======
    def deletar(self):
        try:
            if self.existe == True:
                pasta = os.remove(self.caminho)
            else:
                pass
        except:
            pass

    def situacao(self):
        if os.path.exists(self.caminho):
            return True
        else:
            return False
            
>>>>>>> 474f3bdeaafbf4c21ccf05b07c613f9c4b06fd67
