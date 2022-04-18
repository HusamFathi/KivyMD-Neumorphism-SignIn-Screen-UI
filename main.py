from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.behaviors import RectangularRippleBehavior, BackgroundColorBehavior, CircularRippleBehavior
from kivymd.uix.boxlayout import MDBoxLayout

    
Window.keyboard_anim_args = {'d': 0.5, 't': 'in_out_quart'}
Window.softinput_mode="below_target"
class RectangularRippleButton(MDBoxLayout,
                              RectangularRippleBehavior, ButtonBehavior, BackgroundColorBehavior
                              ):
    pass


class RectangularRippleImage(CircularRippleBehavior, ButtonBehavior, Image):
    pass


class MainApp(MDApp):
   
    def build(self):
        
        self.title = "Sign In Screen"
        self.theme_cls.primary_palette = "Pink"


MainApp().run()
