import operator
import flet as ft
from modello.model import Model
from UI.view import View
class Controller:
    def __init__(self, view:View, model:Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the modello, which implements the logic of the program and holds the data
        self._model = model
        self._albumSelezionato=None
        self._albumSelezionato2=None

    def handleCreaGrafo(self,e):
        self._view._txt_result.controls.clear()
        if self._view._txtCanzoni.value=="":
            self._view.create_alert("Inserire la canzone")
            self._view.update_page()
            return
        try:
            numero=int(self._view._txtCanzoni.value)
        except ValueError:
            self._view.create_alert("Inserire un intero")
            self._view.update_page()
            return
        self._model.creaGrafo(numero)
        self._view._txt_result.controls.append(ft.Text("Grafo creato correttamente "))
        self._view._txt_result.controls.append(ft.Text(f"Vertici : {self._model.numNodes()}"))
        self._view._txt_result.controls.append(ft.Text(f"Archi : {self._model.numEdge()}"))
        self._view._album1.disabled=False
        self._view._adiacenze.disabled=False
        self.fillAlbum1()
        self._view.update_page()

    def handleAdiacenze(self,e):
        self._view._txt_result.controls.clear()
        if self._view._album1 is None:
            self._view.create_alert("Selezionare un album")
            self._view.update_page()
            return
        lista=self._model.getAdiacenze(self._albumSelezionato)
        for elemento in lista:
            self._view._txt_result.controls.append(ft.Text(f"{elemento[0].Title}, bilancio= {elemento[1]}"))
        self._view._path.disabled=False
        self._view._album2.disabled=False
        self._view._txtSoglia.disabled=False
        self.fillAlbum2()
        self._view.update_page()

    def handlePercorso(self,e):
        self._view._txt_result.controls.clear()
        if self._view._album2.value is None:
            self._view.create_alert("Selezionare un album")
            self._view.update_page()
            return
        if self._view._txtSoglia.value=="":
            self._view.create_alert("Inserire la soglia")
            self._view.update_page()
            return
        try:
            numero=int(self._view._txtSoglia.value)
        except ValueError:
            self._view.create_alert("Inserire un intero")
            self._view.update_page()
            return
        lista=self._model.calcolaPercorso(self._albumSelezionato,self._albumSelezionato2,numero)
        if self._albumSelezionato2 in lista:
            self._view._txt_result.controls.append(ft.Text(f"Trovato un percorso con {len(lista)} nodi"))
            for elemento in lista:
                self._view._txt_result.controls.append(ft.Text(elemento.Title))
        else:
            self._view._txt_result.controls.append(ft.Text("Non c'e un percorso"))
        self._view.update_page()

    def fillAlbum1(self):
        album=sorted(self._model.getAlbum(),key=operator.attrgetter("Title"))
        for album in album:
            self._view._album1.options.append(ft.dropdown.Option(text=album.Title,data=album,key=album.AlbumId,on_click=self.selezionaAlbum))
        self._view.update_page()

    def selezionaAlbum(self,e):
        if e.control.data is None:
            self._albumSelezionato=None
        else:
            self._albumSelezionato=e.control.data
            print(self._albumSelezionato)
    def selezionaAlbum2(self,e):
        if e.control.data is None:
            self._albumSelezionato2=None
        else:
            self._albumSelezionato2=e.control.data
            print(self._albumSelezionato2)

    def fillAlbum2(self):
        album=sorted(self._model.getAlbum(),key=operator.attrgetter("Title"))
        for album in album:
            self._view._album2.options.append(ft.dropdown.Option(text=album.Title,data=album,key=album.AlbumId,on_click=self.selezionaAlbum2))
        self._view.update_page()