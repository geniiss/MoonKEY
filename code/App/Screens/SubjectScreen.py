from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder

Builder.load_file("kv_files/SubjectScreen.kv")

class SubjectScreen(Screen):
    subject_code = StringProperty()  # Propietat per mostrar el codi de l'assignatura

    def on_enter(self, *args):
        self.ids.subject_code_label.text = f"Subject Code: {self.subject_code}"

    def go_back(self):
        # Torna a la pantalla principal
        self.manager.current = "statistics"
        # Elimina la pantalla d'assignatura actual després del canvi
        self.manager.remove_widget(self)
