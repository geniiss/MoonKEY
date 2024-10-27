from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder

Builder.load_file("kv_files/SubjectScreen.kv")

class SubjectScreen(Screen):
    subject_code = StringProperty()
    fraction1 = StringProperty("2/6")  # Primera fracció
    fraction2 = StringProperty("3/12") # Segona fracció
    simple_number = StringProperty("3/12")  # Número simple per mostrar
    image_path = StringProperty("../../image/monkeys/angry.png")  # Ruta de la imatge

    def on_enter(self, *args):
        pass

    def go_back(self):
        self.manager.current = "statistics"
        self.manager.remove_widget(self)
