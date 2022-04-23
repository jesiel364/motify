from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard


kv = Builder.load_file('main.kv')

if platform != 'android':
    Window.size= 300, 500

class CardFrase(MDCard):
    frase = StringProperty('')

class Inicio(MDScreen):
    pass

class SM(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(Inicio(name='inicio'))

class Motify(MDApp):
    def build(self):
        # self.theme_cls.theme_style= 'Light'
        # self.theme_cls.primary_color = 'Orange'

        return SM()

if __name__ == '__main__':
    Motify().run()