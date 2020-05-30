#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://docs.python.org/3/library/http.server.html
# https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET

from http.server import BaseHTTPRequestHandler, HTTPServer

class signavio(BaseHTTPRequestHandler):
  def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers()
        message = '{"id": "1", "message": "Hello world"}'
        self.wfile.write(bytes(message, "utf8"))
        return

def run(server_class=HTTPServer, handler_class=signavio):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()

