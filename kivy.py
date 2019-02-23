from kivy.app import App
import pygame
from kivy.uix.button import Button
class Testapp(App):
    def build(self):
        return Button(text="hello siva")
Testapp.run()