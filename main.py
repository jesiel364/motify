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
    Window.size= 350, 570
    
class Item(MDCard):
	text: StringProperty()
	date: StringProperty()

class CardFrase(MDCard):
    frase = StringProperty()
    advice = requests.get('https://api.adviceslip.com/advice').json()
    for key in advice:
        conselho = advice.get(key)['advice']
        frase = conselho
    
    def gerar_frase(self):
        
        advice = requests.get('https://api.adviceslip.com/advice').json()
        for key in advice:
            conselho = advice.get(key)['advice']
            self.ids.lb_frase.text = conselho
            print(conselho)
  
class Inicio(MDScreen):
    pass

class SM(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_widget(Inicio(name='inicio'))

class Motify(MDApp):
    def build(self):
        return SM()
    
if __name__ == '__main__':
    Motify().run()