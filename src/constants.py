import os

host = "localhost"
port = 8080

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_path = os.path.join(base_path, "src")
views_path = os.path.join(base_path, "views")