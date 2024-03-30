from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.properties import NumericProperty, BooleanProperty, StringProperty
class Seconds(Label):
    done = BooleanProperty(False)
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        my_text = 'Прошло секунд: ' + str(self.current)
        super().__init__(text=my_text)

    def restart(self, total, **kwargs):
        pass

    def start(self):
        Clock.schedule_interval(self.change, 1)
        

    def change(self, dt):
        
        self.current += 1
        self.text = 'Прошло секунд:' + str(self.current)
        if self.current >= self.total:
            self.done = True
            return False

