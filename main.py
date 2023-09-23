from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
ScreenManager:
    MainScreen:
    AgendaScreen:

<MainScreen>:
    name: 'main'

    #background settings
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.5, 0.4, 0.7, 1
            Rectangle:
                pos: self.pos
                size: self.size
            #Rectangle:
                pos: self.pos
                size: self.size
                source: "C:/Users/mauro/Documents/GitHub/Lotus/assets/white_gradient.png"

    #here we have the Logo settings
    Image: 
        source: 'C:/Users/mauro/Documents/GitHub/Lotus/assets/logo_instantes.png'
        halign: 'center'
        size_hint: None, None
        size: dp(300), dp(72)
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    #adding buttons

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
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.5, 0.4, 0.7, 1
            Rectangle:
                pos: self.pos
                size: self.size
            #Rectangle:
                pos: self.pos
                size: self.size
                source: "C:/Users/mauro/Documents/GitHub/Lotus/assets/white_gradient.png"
    Button:
        size_hint: None, None
        size: dp(60), dp(60)  # Adjust the size as needed
        pos_hint: {'top': 1.0, 'left': 1.0}
        background_normal: 'C:/Users/mauro/Documents/GitHub/Lotus/assets/left_arrow.png'
        on_release: app.switch_screen('main')

<CajaScreen>:
    name: 'caja'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.5, 0.4, 0.7, 1
            Rectangle:
                pos: self.pos
                size: self.size
            #Rectangle:
                pos: self.pos
                size: self.size
                source: "C:/Users/mauro/Documents/GitHub/Lotus/assets/white_gradient.png"
    Button:
        size_hint: None, None
        size: dp(60), dp(60)  # Adjust the size as needed
        pos_hint: {'top': 1.0, 'left': 1.0}
        background_normal: 'C:/Users/mauro/Documents/GitHub/Lotus/assets/left_arrow.png'
        on_release: app.switch_screen('main')

<VouchersScreen>:
    name: 'vouchers'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.5, 0.4, 0.7, 1
            Rectangle:
                pos: self.pos
                size: self.size
            #Rectangle:
                pos: self.pos
                size: self.size
                source: "C:/Users/mauro/Documents/GitHub/Lotus/assets/white_gradient.png"
    Button:
        size_hint: None, None
        size: dp(60), dp(60)  # Adjust the size as needed
        pos_hint: {'top': 1.0, 'left': 1.0}
        background_normal: 'C:/Users/mauro/Documents/GitHub/Lotus/assets/left_arrow.png'
        on_release: app.switch_screen('main')

<CursosScreen>:
    name: 'cursos'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.5, 0.4, 0.7, 1
            Rectangle:
                pos: self.pos
                size: self.size
            #Rectangle:
                pos: self.pos
                size: self.size
                source: "C:/Users/mauro/Documents/GitHub/Lotus/assets/white_gradient.png"
    Button:
        size_hint: None, None
        size: dp(60), dp(60)  # Adjust the size as needed
        pos_hint: {'top': 1.0, 'left': 1.0}
        background_normal: 'C:/Users/mauro/Documents/GitHub/Lotus/assets/left_arrow.png'
        on_release: app.switch_screen('main')

<FichasScreen>:
    name: 'fichas'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: 0.5, 0.4, 0.7, 1
            Rectangle:
                pos: self.pos
                size: self.size
            #Rectangle:
                pos: self.pos
                size: self.size
                source: "C:/Users/mauro/Documents/GitHub/Lotus/assets/white_gradient.png"
    Button:
        size_hint: None, None
        size: dp(60), dp(60)  # Adjust the size as needed
        pos_hint: {'top': 1.0, 'left': 1.0}
        background_normal: 'C:/Users/mauro/Documents/GitHub/Lotus/assets/left_arrow.png'
        on_release: app.switch_screen('main')

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
