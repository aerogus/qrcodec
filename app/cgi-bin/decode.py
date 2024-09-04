#!/usr/bin/env python3

import io
import cgi
import PIL.Image
import pyzbar.pyzbar

print('Status: 200 OK')
print('Content-Type: text/plain; charset=utf-8')
print('')

form = cgi.FieldStorage()

fileitem = form['img']
if fileitem.filename:
  img = PIL.Image.open(io.BytesIO(fileitem.file.read()))
  data = pyzbar.pyzbar.decode(img)
  print('type:')
  print(data[0])
  print(data[0].type)
  print('')

  print('données:')
  print(data[0].data.decode('utf-8'))
  print('')

  print('qualité:')
  print(data[0].quality)
  print('')

  print('orientation:')
  print(data[0].orientation)
  print('')

  print('raw:')
  print(data[0])

