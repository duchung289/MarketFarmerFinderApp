from kivy.garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu

class MarketMarker(MapMarkerPopup):
    # source = "marker.png"

    market_data = []

    def on_release(self):
        menu = LocationPopupMenu(self.market_data)
        # print("menu: ", menu)
        menu.size_hint =[.8,.9]
        menu.open()

