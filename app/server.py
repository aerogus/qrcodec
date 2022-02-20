#!/usr/bin/env python3

import http.server
import os

PORT = 80

os.chdir(os.path.dirname(__file__))

server_address = ("", PORT)

server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]
print("Serveur actif sur le port :", PORT)

httpd = server(server_address, handler)
try:
  httpd.serve_forever()
except KeyboardInterrupt:
  print("Arrêt du serveur")
  httpd.server_close()
