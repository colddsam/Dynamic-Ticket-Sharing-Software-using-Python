from barcode import Code128
from barcode.writer import ImageWriter
import os
import qrcode
def qrcode_generator(code=""):
    img=qrcode.make(code)
    img.save(os.path.join("qrcode.jpg"))
def barcode_generator(code=""):
    code=Code128(code,writer=ImageWriter())
    code.save("barcode")