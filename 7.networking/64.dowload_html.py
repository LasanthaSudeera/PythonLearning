# using the urllib to download the html page
import urllib.request
try:
    url = urllib.request.urlopen("https://www.google.com")
    content = url.read()
    url.close()
except urllib.error.HTTPError:
    print("Page not found")
    exit()

# Write to a file
f = open("google.html", "wb")
f.write(content)
f.close()