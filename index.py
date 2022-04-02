from bs4 import BeautifulSoup
import requests
import re

url = "https://forums.rpgmakerweb.com/index.php?forums/rgss3-scripts-rmvx-ace.35/"

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

# plugins list on one page
plg = doc.find(class_="structItemContainer-group js-threadList")

# a plugin
item = plg.find("div")

# main div of that plugin
item_main = item.find(class_="structItem-cell--main")

title = item_main.find(class_="structItem-title").a

link = ""

with open("tests.txt", "w") as file:
    file.write(title.string)
    # for i in plg.contents:
    #     file.write(f"{i}\n\n")
    # file.write(doc.contents)

print()
