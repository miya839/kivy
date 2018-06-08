#!/usr/bin/python
#-*- codong: utf-8 -*- 

from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class Calculator(BoxLayout):

    display_text = ObjectProperty()
    #initflag 
    def show_pressed_button(self, text):
        #print "Pressed!: {} Button".format(text)
        self.display_text.text = text 

class DigitalCalcApp(App):
    pass

if __name__ == '__main__':
    Config.set("graphics", "width", "300")
    Config.set("graphics", "height", "400")
    DigitalCalcApp().run()
    


