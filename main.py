from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import Screen, ScreenManager 
import requests
import scraper
from bs4 import BeautifulSoup
Builder.load_file("design.kv")
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

class MainPage(Screen):
    def word_translate(self, word):
        translation = scraper.word_translate(word)
        self.manager.get_screen("tr_page").ids.deffinition.text = "Definition of word "+word
        self.manager.get_screen("tr_page").ids.word.text = word
        self.manager.current = "tr_page"
        print(translation)

class TranslationPage(Screen):
    def word_translate(self, word):


            
            

if __name__ == "__main__":
    MainApp().run()