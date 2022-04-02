from bs4 import BeautifulSoup
import requests
import re

url = "https://forums.rpgmakerweb.com/index.php?forums/rgss3-scripts-rmvx-ace.35/"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

doc = doc.find(class_="structItemContainer-group js-threadList")

divs = doc.contents

print(divs[0])
