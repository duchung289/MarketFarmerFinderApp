from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App

class SearchPopupMeu(MDInputDialog):
    title = "Search By Address"
    text_button_ok = "Search"
    def __init__(self):
        super().__init__()
        self.size_hint = [.9,.3]
        self.events_callback = self.callback

    def callback(self, *args):
        address = self.text_field.text
        # print(address)
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self, address):
        # with open('app_id.txt','r') as f:
        #     app_id = f.read()
        # with open('app_code.txt','r') as f:
        #     app_code = f.read()
        # print(app_id, app_code)
        with open('apiKey.txt', 'r') as f:
            apiKey = f.read()
        address = parse.quote(address)
        # url = "https://geocoder.api.here.com/6.2/geocode.json?searchtext=%s&app_id=%sapp_code=%s" %(address,app_id,app_code)
        url = "https://geocoder.ls.hereapi.com/6.2/geocode.json?searchtext=%s&apiKey=%s" %(address,apiKey)
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)

    def success(self, urlrequest, result):
        # print("Success",result)
        latitude = result["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Latitude"]
        longitude = result["Response"]["View"][0]["Result"][0]["Location"]["NavigationPosition"][0]["Longitude"]
        # print(latitude, longitude)

        app = App.get_running_app()
        mapview = app.root.ids.mapview
        mapview.center_on(latitude,longitude)

    def failure(self, urlrequest, result):
        print("Failure", result)
    def error(self, urlrequest, result):
        print("Error", result)
