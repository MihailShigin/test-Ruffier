# #не забудь импортировать необходимые
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from instructions import txt_instruction
from kivy.uix.textinput import TextInput
from instructions import txt_start
from instructions import txt_test1
from instructions import txt_test2
from instructions import txt_test3
from ruffier import test
from seconds import Seconds
from kivy.core.window import Window
from kivy.uix.widget import Widget


txt = Label(text = 'My first ')
P1 = 0
P2 = 0
P3 = 0
age_text = 0
Name = ''
ruffier_result = 0
blue = (0.5, .7, 1, 1)
Window.clearcolor = blue
Button_color = (0.9, .7, .4, 1)
Button.background_color = Button_color

class ScrButton(Button):
    def __init__(self, screen, orientation = 'horizontal', direction = 'left', goal ='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
        self.orientation = orientation

    def on_press(self):

        if hasattr(self.screen, "next"):
            self.screen.next()
        if self.screen.next_allowed:
            self.screen.manager.transition.direction = self.direction
            self.screen.manager.current = self.goal



class Main(Screen):
    def __init__(self, name='main'):
        super().__init__(name=name)
        
        hl_1 = BoxLayout()
        vl_1 = BoxLayout(orientation='vertical', padding=8)
        vl_2 = BoxLayout(orientation='vertical', padding=8)
        hl_2 = BoxLayout()
        hl_3 = BoxLayout()
        hl_4 = BoxLayout()
        txt = Label(text=txt_start)
        hl_1.add_widget(txt)
        hl_1.add_widget(vl_1)
        btn1 = ScrButton(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5}, screen=self, goal='scr1')
        # btn2 = ScrButton(text='2', screen=self, goal='scr2')
        # btn3 = ScrButton(text='3', screen=self, goal='scr3')
        # btn4 = ScrButton(text='4', screen=self, goal='scr4')
        # btn5 = ScrButton(text='5', screen=self, goal='scr5')
        hl_1.add_widget(btn1)
        # vl.add_widget(btn2)
        # vl.add_widget(btn3)
        # vl.add_widget(btn4)
        # vl.add_widget(btn5)
        vl_2.add_widget(hl_2)
        vl_2.add_widget(hl_3)
        vl_2.add_widget(hl_4)
        self.add_widget(hl_1)
        self.next_allowed = True

class Screen1(Screen):
    def __init__(self, name='scr1'):
        super().__init__(name=name)
        hl = BoxLayout()
        hl_2 = BoxLayout(orientation='horizontal')
        hl_3 = BoxLayout(orientation='horizontal')
        hl_1 = BoxLayout(orientation='horizontal')
        hl_4 = BoxLayout(orientation='horizontal')
        vl = BoxLayout(orientation='vertical')
        vl_2 = BoxLayout(orientation='vertical')
        txt = Label(text=txt_instruction)
        self.textinput = TextInput(size_hint=(0.1, 0.2), pos_hint={'center_y' : 0.2}, text='Name')
        self.textinput_2 = TextInput(size_hint=(0.1, 0.2), pos_hint={'center_y' : 1}, text='Age')
        txt_2 = Label()
        hl.add_widget(vl)
        btn1 = ScrButton(text='Понятно', orientation='horizontal', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5}, screen=self, goal='scr2')
        hl.add_widget(btn1)
        hl_2.add_widget(txt)
        hl_3.add_widget(self.textinput)
        hl_4.add_widget(self.textinput_2)
        vl_2.add_widget(hl_1)
        vl_2.add_widget(hl_2)
        vl_2.add_widget(hl_3)
        vl_2.add_widget(hl_4)
        self.add_widget(hl)
        self.add_widget(vl_2)
        self.next_allowed = True

    def next(self):
        global name
        global age
        name = self.textinput.text
        age_text = self.textinput_2.text
        if age_text.isdigit():
            age = int(age_text)
        else:
            print('Error: please enter a number')
            self.next_allowed = False
            return

        if age <7:
            print('Error: please enter an age of at least 7 years')
            self.next_allowed = False
            return
        self.next_allowed = True

class Screen2(Screen):
    def __init__(self, name='scr2'):
        super().__init__(name='scr2')
        hl = BoxLayout()
        hl_1 = BoxLayout(orientation='horizontal')
        hl_2 = BoxLayout(orientation='horizontal')
        hl_3 = BoxLayout(orientation='horizontal')
        vl = BoxLayout(orientation='vertical', padding=8, spacing=2)
        vl_2 = BoxLayout(orientation='vertical', padding=8, spacing=2)
        txt = Label(text=txt_test1)
        self.seconds = Seconds(15)
        self.textinput = TextInput(size_hint=(0.2, 0.1), pos_hint={'center_y' : 0.5}, text='')
        self.btn1 = ScrButton(text='Дать данные', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5}, screen=self, goal='scr3')
        hl.add_widget(vl)
        hl.add_widget(self.btn1)
        hl_1.add_widget(txt)
        hl_2.add_widget(self.seconds)
        hl_2.add_widget(self.textinput)
        vl_2.add_widget(hl_1)
        vl_2.add_widget(hl_2)
        self.add_widget(hl)
        self.add_widget(vl_2)
        self.seconds.bind(done = self.undisabled)

    def next(self):
        global P1
        global seconds 
        P1_text = self.textinput.text
        if P1_text.isdigit():
            P1 = int(P1_text)
        else:
            print('Error: please enter a number')
            self.next_allowed = False
            return   

        if P1 <26 and P1 > 140:
            print('Error: please enter a pulse in the range from 26 to 140')
            self.next_allowed = False
            return 
        self.next_allowed = True

    def on_enter(self):
        self.seconds.start()
        self.textinput.set_disabled(True)
        self.btn1.set_disabled(True)
        
    def undisabled(self, *args):
            self.textinput.set_disabled(False)
            self.btn1.set_disabled(False)



class Screen3(Screen):
    def __init__(self, name='scr3'):
        super().__init__(name='scr3')
        hl = BoxLayout()
        hl_1 = BoxLayout(orientation='horizontal')
        hl_2 = BoxLayout(orientation='horizontal')
        vl = BoxLayout(orientation='vertical', padding=2, spacing=2)
        vl_2 = BoxLayout(orientation='vertical', padding=2, spacing=2)
        txt = Label(text=txt_test2)
        self.seconds = Seconds(15)
        btn1 = ScrButton(text='Дальше', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5}, screen=self, goal='scr4')
        hl.add_widget(vl)
        hl.add_widget(btn1)
        hl_1.add_widget(txt)
        hl_2.add_widget(self.seconds)
        vl_2.add_widget(hl_1)
        vl_2.add_widget(hl_2)
        self.add_widget(hl)
        self.add_widget(vl_2)
        self.next_allowed = True

    def on_enter(self):
        self.seconds.start()


class Screen4(Screen):
    def __init__(self, name='scr4'):
        super().__init__(name='scr4')
        hl = BoxLayout()
        hl_2 = BoxLayout(orientation='horizontal')
        hl_3 = BoxLayout(orientation='horizontal')
        hl_1 = BoxLayout(orientation='horizontal')
        hl_4 = BoxLayout(orientation='horizontal')
        vl = BoxLayout(orientation='vertical')
        vl_2 = BoxLayout(orientation='vertical')
        txt = Label(text=txt_test3)
        self.textinput = TextInput(size_hint=(0.3, 0.2), pos_hint={'center_y' : 0.2}, text='Результат')
        self.textinput_2 = TextInput(size_hint=(0.3, 0.2), pos_hint={'center_y' : 1}, text='Результат после отдыха')
        txt_2 = Label()
        hl.add_widget(vl)
        btn1 = ScrButton(text='Завершить', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5}, screen=self, goal='scr5')
        hl.add_widget(btn1)
        hl_2.add_widget(txt)
        hl_3.add_widget(self.textinput)
        hl_4.add_widget(self.textinput_2)
        vl_2.add_widget(hl_1)
        vl_2.add_widget(hl_2)
        vl_2.add_widget(hl_3)
        vl_2.add_widget(hl_4)
        self.add_widget(hl)
        self.add_widget(vl_2)

    
    def next(self):
        global P2
        global P3
        P2_text = self.textinput.text
        P3_text = self.textinput_2.text   
        if P2_text.isdigit():
            P2 = int(P2_text)
        else:
            print('Error: please enter a number')
            self.next_allowed = False
            return 
            
        if P3_text.isdigit():
            P3 = int(P2_text)
        else:
            print('Error: please enter a number') 
            self.next_allowed = False
            return 

        if P2 <26 and P2 > 140:
            print('Error: please enter a pulse in the range from 26 to 140')
            self.next_allowed = False
            return 
        if P3 <26 and P3 > 140:
            print('Error: please enter a pulse in the range from 26 to 140')
            self.next_allowed = False
            return 

        self.next_allowed = True   


class Screen5(Screen):
    def __init__(self, name='scr5'):
        super().__init__(name='scr5')
        hl = BoxLayout()
        vl = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.txt = Label(text='Ваш индекс Руфье:')
        hl.add_widget(self.txt)
        hl.add_widget(vl)
        btn1 = ScrButton(text='Вернуться на главный экран', size_hint=(0.3, 0.2), pos_hint={'center_x' : 0.5}, screen=self)
        hl.add_widget(btn1)
        self.add_widget(hl)
        self.on_enter = self.before 

    def before(self):
        global ruffier_result
        ruffier_result = test(P1, P2, P3, age)
        self.txt.text = ruffier_result
        
class MyWidget(Widget):

    def __init__(self):
        super().__init__()
        self.size_hint = 0.2, 1

class MyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        sm = ScreenManager()
        sm.add_widget(Main(name = 'main'))
        sm.add_widget(Screen1(name = 'scr1'))
        sm.add_widget(Screen2(name = 'scr2'))
        sm.add_widget(Screen3(name = 'scr3'))
        sm.add_widget(Screen4(name = 'scr4'))
        sm.add_widget(Screen5(name = 'scr5'))
        return sm
app = MyApp()
app.run()


