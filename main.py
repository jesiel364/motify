from calendar import c
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.utils import platform
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.properties import StringProperty
from kivymd.uix.card import MDCard
from kivymd.uix.list import MDList
import requests
import sqlite3
import datetime

 
kv = Builder.load_file('main.kv')

if platform != 'android':
    Window.size= 350, 570

class Item(MDCard):
    text = StringProperty()
    date = StringProperty()
    frase_id = StringProperty()

    def carregar_recente(self, frase_id):
        conn = sqlite3.connect('advices_db.db')
        conn.row_factory=sqlite3.Row
        # get advices
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM recent_advice where id=?", (frase_id,))
        db = cursor.fetchone()
        print(db['advice'])
        # CardFrase().recente("db['advice']")


class Lista(MDList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
        conn = sqlite3.connect('advices_db.db')
        conn.row_factory=sqlite3.Row
        # get advices
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM recent_advice ORDER BY id DESC")
        db = cursor.fetchall()

        for key in db:
            conselho = key['advice'][:25]
            criado_em = key['criado_em']
            _id = key['id']
            self.add_widget(Item(text=f'{conselho}...', date=criado_em, frase_id=str(_id)))



class CardFrase(MDCard):
    frase = StringProperty()
    advice = requests.get('https://api.adviceslip.com/advice').json()
    for key in advice:
        conselho = advice.get(key)['advice']
        frase = conselho
    
    def gerar_frase(self):
        data = datetime.datetime.now().strftime('%d/%m/%Y ás %H:%M')
        
        advice = requests.get('https://api.adviceslip.com/advice').json()
        for key in advice:
            conselho = advice.get(key)['advice']
            self.ids.lb_frase.text = conselho
            print(conselho)
            conn = sqlite3.connect('advices_db.db')
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(""" 
            INSERT INTO recent_advice (advice, criado_em)
            values (?, ?)
            """, (conselho, str(data)))
            print('Salvo.')
            conn.commit()

    # def recente(self, frase_id):
    #     self.ids.lb_frase.text = 'frase_id'
  
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