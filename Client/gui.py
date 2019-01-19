import kivy
#kivy.require("1.10.1")

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition

class MainScreen(Screen):
    pass

class NameScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

presentation = Builder.load_file("gui.kv")

class Jarvis(App):
    def build(self):
        return presentation
        

if __name__ == "__main__":
    Jarvis().run()