from bs4 import BeautifulSoup
import requests
import re
import json

dns = "https://forums.rpgmakerweb.com"

# For RPG Maker VX Ace plugins
url = "https://forums.rpgmakerweb.com/index.php?forums/rgss3-scripts-rmvx-ace.35/"

# OLD: Testing
# +++++++++++++++++++++++++++++++++++++++++++++++++++
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

# with open("tests.txt", "w") as file:
#     file.write(f"Title: {title.string}\n")
#     file.write(f"Link: {link}\n\n")
# +++++++++++++++++++++++++++++++++++++++++++++++++++

plugin_list = []

with open("plugins.json", "w") as file:
    for i in range(1, 2):
        result = ""
        
        # file.write("\n\n")
        
        if i == 1:
            result = requests.get(url)
        else:
            result = requests.get(f"{url}page-{i}")
        
        doc = BeautifulSoup(result.text, "html.parser")
        plugin_page = doc.find(class_="structItemContainer-group js-threadList")
        plugins = plugin_page.find_all(["div"], class_=re.compile("structItem structItem--thread js-inlineModContainer js-threadListItem.*"))        
        
        # file.write(f"=== Page {i} ===\n\n")
    
        for plugin in plugins:
            plugin_data = {}
            
            main_div = plugin.find(class_="structItem-cell--main")
            
            title = main_div.find(class_="structItem-title").a
            author = main_div.find(class_="username").string
            link = main_div.find(["li"], class_="structItem-startDate").a["href"]
            
            plugin_data = {
                "title": title.string,
                "author": author,
                "link": dns + link,
            }
                        
            plugin_list.append(plugin_data)
            
            # file.write(f"[{author}]\n")
            # file.write(f"\t{title.string}\n")
            # file.write(f"\t{dns}{link}\n\n")
            
    json_obj = json.dumps(plugin_list, indent=4)
    file.write(json_obj)