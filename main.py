from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform
from kivy.core.window import Window
from kivymd.uix.screen import MDScreentext
from kivy import ScreenManager
from kivy.properties import StringProperty

if platform != 'android':
    Window.size= 300, 500

class Inicio(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

class SM(ScreenManagtexter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Inicio(name='inicio'))
def __init__(self, **kw):
        super().__init__(**kw)
class Motify(MDApp):
    def build(self):
        self.theme_cls.theme_style= 'Light'
        self.theme_cls.primary_color = 'Orange'

        return SM()

if __name__ == '__main__':
    Motify().run()

def __init__(self, **kwargs):
        super().__init__(**kwargs)