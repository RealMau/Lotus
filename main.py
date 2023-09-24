from kivy.metrics import dp
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.properties import StringProperty


#default "backbutton" for all pages
class DefaultScreenBackground(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set the background color
        with self.canvas.before:
            Color(0.5, 0.4, 0.7, 1)  # Background color
            self.background_rect = Rectangle(pos=self.pos, size=self.size)

        # Create and add the image
        self.image = Image(
            source='C:/Users/mauro/Documents/GitHub/Lotus/assets/white_gradient.png',
            size_hint=(1, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.add_widget(self.image)

    def on_size(self, instance, value):
        self.background_rect.size = value

    def on_pos(self, instance, value):
        self.background_rect.pos = value




class BackButton(ButtonBehavior, Image):
    destination_screen = StringProperty()

    def __init__(self, destination_screen='', **kwargs):
        super().__init__(**kwargs)
        self.destination_screen = destination_screen
        self.source = 'C:/Users/mauro/Documents/GitHub/Lotus/assets/left_arrow.png'
        self.size_hint = (None, None)
        self.size = (dp(40), dp(40))
        self.pos_hint = {'left': 1.0, 'top': 1.0}

    def on_release(self):
        if self.destination_screen:
            app = MDApp.get_running_app()
            app.switch_screen(self.destination_screen)


KV = '''
ScreenManager:
    MainScreen:
    AgendaScreen:

<MainScreen>:
    name: 'main'

    # Include the DefaultScreenBackground as a child
    DefaultScreenBackground:

    # Here we have the Logo settings
    Image: 
        source: 'C:/Users/mauro/Documents/GitHub/Lotus/assets/logo_instantes.png'
        halign: 'center'
        size_hint: None, None
        size: dp(300), dp(72)
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}


     #Agenda
    MDRectangleFlatButton:
        text: "Agenda"
        theme_text_color: "Custom"
        text_color: "black"
        line_color: "purple"
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}
        font_size: '24sp'
        size_hint: 0.4, None
        on_release: app.switch_screen('agenda')
    #Caja
    MDRectangleFlatButton:
        text: "Caja"
        theme_text_color: "Custom"
        text_color: "black"
        line_color: "purple"
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        font_size: '24sp'
        size_hint: 0.4, None
        on_release: app.switch_screen('caja')
    #Vouchers
    MDRectangleFlatButton:
        text: "Vouchers"
        theme_text_color: "Custom"
        text_color: "black"
        line_color: "purple"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        font_size: '24sp'
        size_hint: 0.4, None
        on_release: app.switch_screen('vouchers')
    #Cursos
    MDRectangleFlatButton:
        text: "Cursos"
        theme_text_color: "Custom"
        text_color: "black"
        line_color: "purple"
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        font_size: '24sp'
        size_hint: 0.4, None
        on_release: app.switch_screen('cursos')
    #Fichas
    MDRectangleFlatButton:
        text: "Fichas"
        theme_text_color: "Custom"
        text_color: "black"
        line_color: "purple"
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        font_size: '24sp'
        size_hint: 0.4, None
        on_release: app.switch_screen('fichas')

<AgendaScreen>:
    name: 'agenda'
    DefaultScreenBackground:
    BackButton:
        destination_screen: 'main'

<CajaScreen>:
    name: 'caja'
    DefaultScreenBackground:
    BackButton:
        destination_screen: 'main'

<VouchersScreen>:
    name: 'vouchers'
    DefaultScreenBackground:
    BackButton:
        destination_screen: 'main'

<CursosScreen>:
    name: 'cursos'
    DefaultScreenBackground:
    BackButton:
        destination_screen: 'main'

<FichasScreen>:
    name: 'fichas'
    DefaultScreenBackground:
    BackButton:
        destination_screen: 'main'

'''


class MainScreen(Screen):
    pass


class AgendaScreen(Screen):
    pass


class CajaScreen(Screen):
    pass


class VouchersScreen(Screen):
    pass


class CursosScreen(Screen):
    pass


class FichasScreen(Screen):
    pass


class MainApp(MDApp):
    def build(self):
        self.title = 'Lotus'
        self.kv = Builder.load_string(KV)
        self.sm = ScreenManager()
        self.sm.add_widget(MainScreen(name='main'))
        self.sm.add_widget(AgendaScreen(name='agenda'))
        self.sm.add_widget(CajaScreen(name='caja'))
        self.sm.add_widget(VouchersScreen(name='vouchers'))
        self.sm.add_widget(CursosScreen(name='cursos'))
        self.sm.add_widget(FichasScreen(name='fichas'))
        return self.sm

    def switch_screen(self, screen_name):
        self.sm.current = screen_name


if __name__ == '__main__':
    MainApp().run()
