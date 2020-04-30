from Lib import os

class Pasta():

    def __init__(self, caminho):
        self.caminho = caminho
        self.existe = self.situacao()

    def criar(self):
        try:
            if self.existe == False:
                pasta = os.makedirs(self.caminho)
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
            
