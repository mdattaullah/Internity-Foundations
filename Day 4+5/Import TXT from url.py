import urllib
import requests
url = "https://raw.githubusercontent.com/rjrealworld/Internity-Foundations/main/Day%204%2B5/War%20and%20Peace.txt"
file = urllib.request.urlopen(url)

for line in file:
	decoded_line = line.decode("utf-8")
	print(decoded_line)
