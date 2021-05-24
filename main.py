from kivy.app import App
from kivy.lang import Builder 
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
import scraper
Builder.load_file("design.kv")
class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

class MainPage(Screen):
    def word_translate(self, word):
        translation = scraper.word_translate(word)
        self.manager.get_screen("tr_page").ids.word.text = "Definition of word "+word
        self.manager.current = "tr_page"
        #self.manager.get_screen("tr_page").ids.defs
        for i in range(len(translation)):
            label_number = Label(text=str(i+1))
            label_def = Label(text=translation[i][1])
            label_type = Label(text=translation[i][0])
            self.ids.defs.add_widget(label_number)
            self.ids.defs.add_widget(label_def)
            self.ids.defs.add_widget(label_type)
        #print(translation)
        

class TranslationPage(Screen):
    def go_back(self):
        self.manager.current="main_page"
        self.ids.defs.clear_widgets()
    # def word_translate(self, word):
    #     self.manager.get_screen("tr_page").ids.deffinition.text = "Definition of word "+word
    #     self.manager.get_screen("tr_page").ids.word.text = word
class ImageButton(ButtonBehavior, Image):
    pass
            
            

if __name__ == "__main__":
    MainApp().run()