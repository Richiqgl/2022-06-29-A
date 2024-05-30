import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff

        self._page = page
        self._page.title = "2022-06-29-A"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._btnCreagrafo = None
        self._txtCanzoni= None
        self._ddcanzone = None
        self._album1=None
        self._album2 = None
        self._adiacenze=None
        self._txtSoglia=None
        self._txtInMemoria=None
        self._txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("ESAME A- 29-06-2022", color="blue", size=24)
        self._page.controls.append(self._title)

        #ROW with  controls
        self._txtCanzoni = ft.TextField(label="Canzoni")
        self._btnCreagrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([self._txtCanzoni, self._btnCreagrafo],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)


        self._album1 = ft.Dropdown(label="Album1",width=500,disabled=True)
        self._adiacenze = ft.ElevatedButton(text="Stampa Adiacenze", on_click=self._controller.handleAdiacenze,disabled=True)
        row2 = ft.Row([ self._album1 ,self._adiacenze],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)

        self._album2=ft.Dropdown(label="Album2",width=500,disabled=True)
        self._path=ft.ElevatedButton(text="Cerca Percorso ",on_click=self.controller.handlePercorso,disabled=True)
        row3=ft.Row([self._album2,self._path ],alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)

        self._txtSoglia=ft.TextField(label="Soglia",disabled=True)
        row4=ft.Row([self._txtSoglia], alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row4)

        # List View where the reply is printed
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self._txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def update_page(self):
        self._page.update()

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()