# python-web-server

python-web-server

## Requirements

Python 3

http module

urllib module

## Usage

Run the command below.

"""
py main.py
"""

The web server will be running on port 8080.

So, you can access the web page on http://localhost:8080/.

## Routes

If you want to specify your own route, open ./src/routes.py, and you will find something like this.

"""
routes = {
    "/": "hello.html",
    "/hello": "hello.html"
}
"""

Add new element into the dictionary, set the key as your route and the value as your file name.

## Views

If you want to make a file for the web page, you have to add new HTML file into ./view/ folder.
