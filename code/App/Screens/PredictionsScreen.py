from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivymd.uix.list import OneLineListItem

llista_nota : dict[int, float] = {
    12: 4.5,
    13: 5.5,
    14: 6.5,
    15: 7.32
}

llista_assigs = {
    12: "Mates",
    13: "Llengua",
    14: "Anglès",
    15: "Tecnologia"
}

Builder.load_file("kv_files/PredictionsScreen.kv")

class PredictionsScreen(Screen):
    assignments = ListProperty([])

    def on_enter(self):
        # Netegem la llista per evitar duplicats quan es torna a entrar a la pantalla
        self.ids.predictions_list.clear_widgets()
        
        # Afegim elements a `predictions_list`
        for key in llista_assigs:
            subject = llista_assigs[key]
            grade = f"{llista_nota[key]:.2f}"
            self.ids.predictions_list.add_widget(OneLineListItem(text=f"{subject}: {grade}"))
