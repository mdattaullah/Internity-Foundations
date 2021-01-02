import urllib
import requests
url = "http://www.gutenberg.org/files/2600/2600-0.txt"
file = urllib.request.urlopen(url)

for line in file:
	decoded_line = line.decode("utf-8")
	print(decoded_line)