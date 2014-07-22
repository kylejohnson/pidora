import os

current_dir = os.path.dirname(os.path.abspath(__file__)) + "/"

def index(songData):
	return open(current_dir + "static/html/index.html").read()
