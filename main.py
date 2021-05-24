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
        scroll = ScrollView()
        self.manager.get_screen("tr_page").ids.main.add_widget(scroll)
        layout = GridLayout(cols=1,)
        for i in range(len(translation)):
            label_number = Label(text=str(i+1), size_hint=(1, None))
            label_def = Label(text = translation[i][1], size_hint=(1, None))
            label_def.bind(width=lambda *x:label_def.setter('text_size')(label_def,(label_def.width, None)))
            

            label_type = Label(text=translation[i][0], size_hint=(1, None))
            layout = GridLayout(cols=3)
            self.manager.get_screen("tr_page").ids.defs.add_widget(label_number)
            self.manager.get_screen("tr_page").ids.defs.add_widget(label_def)
            self.manager.get_screen("tr_page").ids.defs.add_widget(label_type)
        # label.bind(
        # width=lambda *x: label.setter('text_size')(label, (label.width, None)))
        

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