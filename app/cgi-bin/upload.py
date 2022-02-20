#!/usr/bin/env python3

import io
import cgi
import PIL.Image
import pyzbar.pyzbar
import pprint

print('Status: 200 OK')
print('Content-Type: text/plain; charset=utf-8')
print('')

form = cgi.FieldStorage()
pp = pprint.PrettyPrinter()

fileitem = form['pass']
if fileitem.filename:
  img = PIL.Image.open(io.BytesIO(fileitem.file.read()))
  data = pyzbar.pyzbar.decode(img)
  pp.pprint(data)
