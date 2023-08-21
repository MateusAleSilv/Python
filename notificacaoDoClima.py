import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()

def getdata(url):
    r = requests.get(url)
    return r.text

htmldata = getdata("https://www.google.com/search?q=tempo+florian%C3%B3polis&oq=tempo+flori&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDQxMTdqMGo0qAIAsAIA&sourceid=chrome&ie=UTF-8")
soup = BeautifulSoup(htmldata, 'html.parser')
print(soup.prettify())

current_temp = soup.find_all("span",
                             class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
chances_rain = soup.find_all("div",
                             class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

temp = (str(current_temp))
temp_rain = str(chances_rain)

result = "current_temp " + temp[128:-9] + "  in patna bihar" + "\n" + temp_rain[131:-14]

n.show_toast("Weather update", result, duration = 10)
