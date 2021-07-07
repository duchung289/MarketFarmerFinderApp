from kivymd.app import MDApp
from kivy.core.window import Window
Window.size = (400,800)
from farmersmapview import FarmersMapView
import sqlite3
from searchpopupmenu import SearchPopupMenu
from gpshelper import GpsHelper


class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None
    def on_start(self):
        self.theme_cls.primary_pallete ="BlueGray"

        GpsHelper().run()

        self.connection = sqlite3.connect("markets.db")
        self.cursor = self.connection.cursor()

        self.search_menu = SearchPopupMenu()

if __name__ == "__main__":
    MainApp().run()