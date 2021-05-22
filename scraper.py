import requests
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
        all_results.append(["No exact matches for word %s" %(word), "Here are the nearest results"], )
        results = soup.find("ul", {"class": "search-results unpadded"}).find_all("li")
        for result in results:
            all_results.append(result.find("a").text)
        
    if len(types) > 4:
        limit = 4
    else:
        limit = len(types)
    for i in range(limit):
        deffinition_type = types[i].find("h3").text
        p = types[i].find_all("p")
        for item in p:
            deffinition = item.find("span", {"class":"ind"})
            if deffinition:
                all_results.append([deffinition_type, deffinition.text])
    return all_results