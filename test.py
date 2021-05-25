from kivy.app import App 
from kivy.animation import Animation

class MainApp(App):
    def animate_the_buttons(self, widget, *args):
        anim = Animation(background_color=(1, 0, 0, 1))
        anim.start(widget)

MainApp().run()