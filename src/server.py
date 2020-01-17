import os
from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler
from .constants import *
from .routes import routes

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        for route, filename in routes.items():
            if urlparse(self.path).path.lstrip("/") == route.lstrip("/"):
                self.path = os.path.join(views_path, filename)

        try:
            file_to_open = open(self.path).read()
            self.send_response(200)
        except:
            file_to_open = "File not found!"
            self.send_response(404)

        self.end_headers()
        self.wfile.write(bytes(file_to_open, "utf-8"))
