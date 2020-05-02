from Lib import os,shutil
import arquivo as Arquivo

class Pasta():

    def __init__(self, caminho):
        self.caminho = caminho
        self.existe = self.situacao()

    def criar(self):
        try:
            if self.existe == False:
                os.makedirs(self.caminho)
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
        try:
            if caminho == True:
                lista = os.listdir(self.caminho)
            else:
                lista = os.listdir(caminho)
            return lista
        except:
            pass

    def arrumarPastas(self,separador, arg=False):
        try:
            lista = self.listar()
            for item in lista:
                arquivo = Arquivo.Arquivo(item,self.caminho)
                if os.path.isfile(arquivo.path):
                    x = arquivo.nome.split('.')[0]                
                    x = x.split(separador)
                    if arg != False:
                        for a in arg:
                            arquivo.diretorio = arquivo.diretorio + x[a] + '\\'
                            pastax = Pasta(arquivo.diretorio)
                            pastax.criar()
                    else:
                        for a in x:
                                nomeArquivo = nomeArquivo + a + '\\'
                                pastax = Pasta(nomeArquivo)
                                pastax.criar()
                    arquivo.mover(arquivo.diretorio + arquivo.nome)
                else:
                    continue
        except:
            pass


