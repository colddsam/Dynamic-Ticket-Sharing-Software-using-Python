import cv2
import os
from PIL import Image
from barcodeprod import qrcode_generator,barcode_generator

def imagegen(code=""):
    ticket=Image.open(os.path.join("images","template.jpg"))
    barcode_generator(code=code)
    barcode=Image.open(os.path.join(os.path.join("barcode.png")))
    barcode_re=barcode.resize(
        (320,84)
    )

    ticket.paste(barcode_re,(378,886))
    ticket.save("ticket.jpg")