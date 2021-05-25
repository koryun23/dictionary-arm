import requests
import re
from bs4 import BeautifulSoup

def word_translate(word):
    word=word.lower()
    url = "https://www.lexico.com/definition/"+word
    r = requests.get(url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all_results = []
    types = soup.find_all("section", {"class":"gramb"})
    if not types:
        return ["No such word. Please check the\n spelling."]
    else:
        if len(types) > 4:
            limit = 4
        else:
            limit = len(types)
        for i in range(limit):
            p = types[i].find_all("p")
            for item in p:
                deffinition = item.find("span", {"class":"ind"})
                if deffinition:
                
                    deff = re.sub("(.{30})", "\\1\n", deffinition.text, 0, re.DOTALL)

                    all_results.append([deff])
    return all_results
print(word_translate("home"))