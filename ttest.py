from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        padding:200
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'Brushed background.png' 
        BoxLayout:                         
            spacing: dp(7)
            BoxLayout:
                padding: 20
                # CHANGE to canvas for proper trasition
                canvas.after:
                    Color:
                        rgba:[0,0,0,1]
                    Line:
                        width:dp(8)
                        rounded_rectangle: (*self.pos,self.width,self.height, 2)
                Button:
                    text: 'Go To Editor'
                    on_press: root.manager.current = 'editor'

            
<EditorScreen>:
    BoxLayout:
        padding:200
        canvas.before:
            Rectangle:
                pos: self.pos
                size: self.size
                source:'Brushed background.png'
        BoxLayout:                         
            spacing: dp(7)
            BoxLayout:
                padding: 20
                # CHANGE TO canvas for proper transition
                canvas.after:  
                    Color:
                        rgba:[0,0,0,1]
                    Line:
                        width:dp(8)
                        rounded_rectangle: (*self.pos,self.width,self.height, 2)
                Button:
                    text: 'Go to Menu'
                    on_press:root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
    pass


class EditorScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.transition = SlideTransition(duration=2)
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(EditorScreen(name='editor'))

class TestApp(App):

    def build(self):
        return sm

TestApp().run()