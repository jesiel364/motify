from calendar import c
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
import requests


kv = Builder.load_file('main.kv')

if platform != 'android':
    Window.size= 300, 500

class CardFrase(MDCard):

    frase = StringProperty()
    
    def gerar_frase(self):
        
        advice = requests.get('https://api.adviceslip.com/advice').json()
        for key in advice:
            conselho = advice.get(key)['advice']
            self.frase = conselho
            print(conselho)
            # frase=conselho

    

    
    
    
class Inicio(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

    

class SM(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

        self.add_widget(Inicio(name='inicio'))

class Motify(MDApp):
   
    def build(self):
        # self.theme_cls.theme_style= 'Light'
        # self.theme_cls.primary_color = 'Orange'
        return SM()
    
    def on_start(self):
        CardFrase().gerar_frase()
        advice = requests.get('https://api.adviceslip.com/advice').json()
        for key in advice:
            conselho = advice.get(key)['advice']
            CardFrase().frase = conselho
            print(conselho)

        

if __name__ == '__main__':
    Motify().run()