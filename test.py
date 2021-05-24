from kivy.app import App 
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.label import Label
from kivy.lang import Builder
Builder.load_file("test.kv")

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

class Page(Screen):
    def show(self):

        for i in range(300):
            label = Label(text= "Some text", size_hint=(1, None))
            self.ids.defs.add_widget(label)
if __name__ == "__main__":
    MainApp().run()