import pyqrcode
import png

adress = input("Import your url: ")
url = pyqrcode.create(adress)
url.png('qrcode.png', scale = 8)
