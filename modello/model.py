import copy

import networkx as nx

from database.DAO import DAO

class Model():
    def __init__(self):
        self._grafo=nx.DiGraph()
        self._album=None
        pass

    def creaGrafo(self, numero):
        self._grafo.clear()
        self._album=DAO.getAlbum(numero)
        self._grafo.add_nodes_from(self._album)
        for u in self._grafo.nodes:
            for v in self._grafo.nodes:
                if u!=v:
                    if (u.Conteggio-v.Conteggio)!=0:
                        if u.Conteggio>v.Conteggio:
                            self._grafo.add_edge(v,u,weight=abs(u.Conteggio-v.Conteggio))
                        else:
                            self._grafo.add_edge(u, v, weight=abs(u.Conteggio - v.Conteggio))
        return self._grafo
    def numNodes(self):
        return len(self._grafo.nodes)

    def numEdge(self):
        return len(self._grafo.edges)
    def getAlbum(self):
        if self._album is None:
            print("Non ci sono ancora gli album")
            return
        return self._album

    def getAdiacenze(self,albumSelezionato):
        self.dizionario={}
        lista=[]
        for u in self._grafo.nodes:
            sommaE=0
            sommaU=0
            entranti=list(self._grafo.in_edges(u,data=True))
            for v in entranti:
                sommaE+=v[2]["weight"]
            uscenti=list(self._grafo.out_edges(u,data=True))
            for s in uscenti:
                sommaU+=s[2]["weight"]
            self.dizionario[u]=sommaE-sommaU
        tree = nx.dfs_tree(self._grafo, albumSelezionato)
        successori = list(tree.nodes)[1:]
        for (chiave,valore) in self.dizionario.items():
            if chiave in successori:
                lista.append((chiave,valore))
        lista.sort(key=lambda v:v[1],reverse=True)
        #print(list(self._grafo.neighbors(albumSelezionato)))
        return lista

    def calcolaPercorso(self,album1,album2,soglia):
        self.bestpath=[]
        parziale=[album1]

        self.ricorsione(parziale,album2,album1,soglia)

        return self.bestpath


    def ricorsione(self, parziale, album2,album1,soglia):
        if len(parziale)>len(self.bestpath):
            self.bestpath=copy.deepcopy(parziale)
        if parziale[-1]==album2:
            return
        for vertice in self._grafo.neighbors(parziale[-1]):
                if vertice not in parziale and self.dizionario[vertice]>self.dizionario[album1] and self._grafo[parziale[-1]][vertice]["weight"]>=soglia:
                    parziale.append(vertice)
                    self.ricorsione(parziale,album2,album1,soglia)
                    parziale.pop()



if __name__=="__main__":
    myModel=Model()
    myModel.creaGrafo(18)
    print(myModel.numNodes())
    print(myModel.numEdge())


    # def getAdiacenze(self,albumSelezionato):
    #     lista=[]
    #     tree = nx.dfs_tree(self._grafo, albumSelezionato)
    #     successori = list(tree.nodes)[1:]
    #     for u in successori:
    #         sommaE=0
    #         sommaU=0
    #         entranti=list(self._grafo.in_edges(u,data=True))
    #         for v in entranti:
    #             sommaE+=v[2]["weight"]
    #         uscenti=list(self._grafo.out_edges(u,data=True))
    #         for s in uscenti:
    #             sommaU+=s[2]["weight"]
    #         lista.append((u.Title,sommaE-sommaU))
    #     lista.sort(key=lambda v:v[1],reverse=True)
    #     print(len(lista))
    #     return lista