#!/usr/bin/env python3

import cgi
import qrcode
import qrcode.image.svg
import sys

form = cgi.FieldStorage()
content = form.getvalue('content')

#qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5, image_factory=qrcode.image.svg.SvgPathImage)

qr.add_data(content)
qr.make(fit = True)

img = qr.make_image(fill = "black", back_color = "white")
#img.save("qrcode.svg")

print('Status: 200 OK')
print('Content-Type: image/svg+xml')
print('')
print(img.to_string().decode('utf-8'))
