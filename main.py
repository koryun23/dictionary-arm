from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import Screen, ScreenManager 
import requests
from bs4 import BeautifulSoup
Builder.load_file("design.kv")
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

class MainPage(Screen):
    def word_translate(self, word):

        url = "https://www.lexico.com/definition/"+word.lower()
        print(url)
        r = requests.get(url)
        c = r.content
        soup = BeautifulSoup(c, "html.parser")
        # print(soup.find_all("ol", {"class":"_1Mc81"}))
        types = soup.find_all("section", {"class":"gramb"})
        if not types:
            print("No exact matches for word %s" %(word))
            print("Here are the nearest results")
            results = soup.find("ul", {"class": "search-results unpadded"}).find_all("li")
            for result in results:
                print(result.find("a").text)

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
                    print(deffinition_type, deffinition.text)
        self.manager.get_screen("tr_page").ids.deffinition.text = "Definition of word "+word
        self.manager.current = "tr_page"
        # for i in range(len(types)):
        #     print(i+1, types[i].text)
class TranslationPage(Screen):
    pass


            
            

if __name__ == "__main__":
    MainApp().run()