from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (400,800)
from farmersmapview import FarmersMapView
import sqlite3
from searchpopupmenu import SearchPopupMeu


class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None
    def on_start(self):
        self.connection = sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()

        self.search_menu = SearchPopupMeu()

if __name__ == "__main__":
    MainApp().run()