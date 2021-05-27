import requests
import re
import imp
import sys

class ImportBlocker(object):

    def __init__(self, *args):
        self.black_list = args

    def find_module(self, name, path=None):
        if name in self.black_list:
            return self

        return None

    def load_module(self, name):
        module = imp.new_module(name)
        module.__all__ = [] # Necessary because of how bs4 inspects the module

        return module

sys.meta_path = [ImportBlocker('bs4.builder._htmlparser')]
from bs4 import BeautifulSoup

def word_translate(word):
    word=word.lower()
    url = "https://www.lexico.com/definition/"+word
    try:    
        r = requests.get(url)
    except:
        return ["Please Check your\ninternet connection"]
    c = r.content
    soup = BeautifulSoup(c, "html.parser")
    all_results = []
    types = soup.find_all("section", {"class":"gramb"})
    if not types:
        return ["No such word."]
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
                
                    deff = re.sub("(.{25})", "\\1\n", deffinition.text, 0, re.DOTALL)

                    all_results.append([deff])
    return all_results
print(word_translate("home"))