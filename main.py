from kivy.app import App
from kivymd.app import MDApp
from kivy.lang import Builder 
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import scraper
Builder.load_file("design.kv")

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

class MainPage(Screen):
    def word_translate(self, word):
        if word!='' and ' ' not in word:
            self.ids.defs.clear_widgets()
            translation = scraper.word_translate(word)
            if translation:
                if type(translation[0]) == str:
                    self.ids.entered_word.text = translation[0]
                else:
                    self.ids.entered_word.text = word
                    print(translation)
                    for i in range(len(translation)):
                        label_def = Label(text = str(i+1)+"."+translation[i][0], size_hint=(1, None), color=(150/255, 40/255, 27/255, 1))

                        self.ids.defs.add_widget(label_def)
            else:
                self.ids.entered_word.text = "No such word."
        else:
            self.ids.defs.clear_widgets()
            self.ids.entered_word.text = "Please enter\na single word."
        


class ImageButton(ButtonBehavior, Image):
    pass
            
            

if __name__ == "__main__":
    MainApp().run()
