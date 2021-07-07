from kivy.app import App
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog

class GpsHelper():
    has_centered_map = False
    def run(self):
        # Get a reference to GPS Blinker, then call blink()
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker

        # Start blinking the GPS Blinker
        gps_blinker.blink()

        # Request permission on Android
        if platform == "android":
            from android.permissions import Permission, request_permissions
            def callback(permission, results):
                if all([res for res in results]):
                    print("Got all permission")
                else:
                    print("Did not get permission")

            request_permissions([Permission.ASSESS_COARSE_LOCATION,Permission.ASSESS_FIND_LOCATION], callback)

        # Configure GPS
        if platform == "android" or platform =="ios":
            from plyer import gps
            gps.configure(on_location=self.update_blinker_position,
                          on_status=self.on_auth_status)
            gps.start(minTime=1000, minDistance=0)

    def update_blinker_position(self, *args, **kwargs):
        my_lat = kwargs['lat']
        my_lon = kwargs['lon']
        my_lat = 30
        my_lon = 30
        print("GPS POSITION:", my_lat, my_lon)

        # Update the gps blinker position
        gps_blinker = App.get_running_app().root.ids.mapview.ids.blinker
        gps_blinker.lat = my_lat
        gps_blinker.lon = my_lon

        #Center map on gps
        if not has_centered_map:
            map = App.get_running_app().ids.mapview
            map.center_on(my_lat,my_lon)
            self.has_centered_map = True

    def on_auth_status(self, general_status, status_message):
        if general_status == "provider_enabled":
            pass
        else:
            self.open_gps_assess_popup()

    def open_gps_assess_popup(self):
        dialog = MDDialog(title='GPS ERROR', text='You need to enable GPS assess!')
        dialog.size_hint = [.8,.8]
        dialog.pos_hint = {'center_x':.5, 'center_y':.5}
        dialog.open()
