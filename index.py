from bs4 import BeautifulSoup
import requests
import re

dns = "https://forums.rpgmakerweb.com"
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
link = item_main.find(["li"], class_="structItem-startDate").a["href"]

print(link)

with open("tests.txt", "w") as file:
    file.write(f"Title: {title.string}\n")
    file.write(f"Link: {link}\n\n")

print()

plugin_page = doc.find(class_="structItemContainer-group js-threadList")

plugins = plugin_page.find_all(["div"], class_=re.compile("structItem structItem--thread js-inlineModContainer js-threadListItem.*"))

with open("tests2.txt", "w") as file:
    for plugin in plugins:
        main_div = plugin.find(class_="structItem-cell--main")
        title = main_div.find(class_="structItem-title").a
        aaa = main_div.find(["li"], class_="structItem-startDate").a["href"]
        
        file.write(f"Title: {title.string}\n")
        file.write(f"Link: {dns}{aaa}\n\n")
        
        # file.write(f"{plugin.prettify()}\n")
