from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class TestImageApp(App):
    def build(self):
        image = Image(source = r"C:\Users\TDANAM\Downloads\pics\franken collar1.png",
                      size_hint=(.5,.5),
                      pos_hint = {'center_x' : .5, 'center_y': .5})
        return image

if __name__ == "__main__":
    app = TestImageApp()
    app.run()