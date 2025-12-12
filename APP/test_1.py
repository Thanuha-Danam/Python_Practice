from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        label = Label(text= "Hello this is my first App using Kivy",
                      size_hint = (.10, .10),
                      pos_hint = {'center_x': .45, 'center_y': .55})
        return label
    
if __name__ == "__main__":
    app = TestApp()
    app.run()