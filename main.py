from http.server import HTTPServer
from src.server import Server
from src.constants import *

httpd = HTTPServer((str(host), int(port)), Server)
httpd.serve_forever()
