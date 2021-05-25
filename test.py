from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout 
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

        for i in range(2):
            label = Label(text= "Some text "*10,  size_hint=(1,None))
            label.bind(width=lambda *x:label.setter('text_size')(label,(label.width, None)),
            texture_size=lambda *x:label.setter('height')(label,label.texture_size[1]))
            
            self.ids.defs.add_widget(label)
if __name__ == "__main__":
    MainApp().run()