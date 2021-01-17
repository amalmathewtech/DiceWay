from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout

import random

class First_Screen(Screen):

    def update(self):
        self.numbers = random.randint(1, 6)
        self.ids.dice.background_normal=str(self.numbers)+ ".png"

class ScreenManagement(ScreenManager):
    pass

GUI = Builder.load_file("main.kv")

class DiceWayApp(App):
    def build(self):
        return GUI

DiceWayApp().run()
