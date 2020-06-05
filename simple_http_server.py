#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://docs.python.org/3/library/http.server.html
# https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET

from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import requests


class hello_world(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        message = '{"id": "1", "message": "Hello world"}'
        self.wfile.write(bytes(message, "utf8"))
        return


def runone(server_class=HTTPServer, handler_class=hello_world):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    thread = threading.Thread(target=httpd.handle_request())
    thread.start()

def run(server_class=HTTPServer, handler_class=hello_world):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    thread = threading.Thread(target=httpd.serve_forever())
    thread.start()


if __name__ == "__main__":
    runone()
#    requests.get("http://localhost:8000").json()

