#!/usr/bin/python
#-*- codong: utf-8 -*- 

import qrcode

#1Nem = 1000000mosaic 

address = "NDOZFGZTFYVSKHGCSPZEFKM2WFQSXM66M5MCHYNP"
mosaic = 1000000
message = "test"
wallet_name = "test"

class QR():

    def __init__(self):
        pass

    def make(self, amount,file_name):

        self.send_amount = amount * mosaic
        print self.send_amount
        qrdata = '{"v":2,"type":2,"data":{"addr":"' + address + '","amount":' + str(self.send_amount) + ',"msg":"' + message + '","name":"' + wallet_name + '"}}'

        qr = qrcode.QRCode(
                version = 2,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=6,
                border=4,
                )
        qr.add_data(qrdata)
        qr.make(fit=True)
        img = qr.make_image(fill_color="white", back_color="black")
        img.save('./image/' + file_name + '.bmp')
 
