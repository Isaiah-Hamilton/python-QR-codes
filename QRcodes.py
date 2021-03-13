import pyqrcode
import png
from pyqrcode import QRCode
QRString = "..........................................." # Paste any url here
url = pyqrcode.create(QRString)
url.png('Desktop/qr.png', scale = 8)