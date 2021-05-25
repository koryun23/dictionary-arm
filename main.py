from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView
from kivy.config import Config

import scraper
Builder.load_file("design.kv")
Config.set('graphics', 'resizable', '0') #0 being off 1 being on as in true/false
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '700')
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

class MainPage(Screen):
    def word_translate(self, word):
        self.ids.defs.clear_widgets()
        translation = scraper.word_translate(word)
        self.ids.entered_word.text = word
        for i in range(len(translation)):
            label_def = Label(text = str(i+1)+"."+translation[i][1], size_hint=(1, None), color=(0,0,0,1))

            self.ids.defs.add_widget(label_def)
        


class ImageButton(ButtonBehavior, Image):
    pass
            
            

if __name__ == "__main__":
    MainApp().run()