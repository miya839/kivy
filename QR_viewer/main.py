#!/usr/bin/python
#-*- codong: utf-8 -*- 

import os
from make_QR import QR

from kivy.config import Config

from kivy.app import App
from kivy.uix.widget import Widget

from kivy.properties import StringProperty

from kivy.resources import resource_add_path

resource_add_path('./image')

class ImageWidget(Widget):
    if os.path.exists('./image/qr.bmp') == False:
        QR().make(0, 'qr')
    source = StringProperty('./image/qr.bmp') 

    def __init__(self, **kwargs):    
        super(ImageWidget, self).__init__(**kwargs)
        pass

    def buttonClicked(self):
        if os.path.exists('./image/qr1.bmp') == False:
            QR().make(100, 'qr1')
        self.source = './image/qr1.bmp'


    def buttonClicked2(self):
        if os.path.exists('./image/qr2.bmp') == False:
            QR().make(200, 'qr2')
        self.source = './image/qr2.bmp'
         
    def buttonClicked3(self):
        if os.path.exists('./image/qr3.bmp') == False:
            QR().make(300, 'qr3')
        self.source = './image/qr3.bmp'

    def buttonClicked4(self):
        if os.path.exists('./image/qr' +  self.ids["text_box"].text + '.bmp') == False:
            QR().make(int(self.ids["text_box"].text), 'qr' + self.ids["text_box"].text)
        self.source = './image/qr' + self.ids["text_box"].text + '.bmp'
    
class TestApp(App):
    def __init__(self, **kwargs):
        super(TestApp, self).__init__(**kwargs)
        self.title = 'view image'

if __name__ == '__main__':
    TestApp().run()
    


