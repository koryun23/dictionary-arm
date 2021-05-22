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

        url = "https://www.lingvolive.com/en-us/"+"translate/en-ru/"+word.lower()
        print(url)
        # r = requests.get(url)
        # c = r.content
        # soup = BeautifulSoup(c, "html.parser")
        # print(soup.find_all("ol", {"class":"_1Mc81"}))


if __name__ == "__main__":
    MainApp().run()