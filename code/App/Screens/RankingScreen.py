from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_file("kv_files/RankingScreen.kv")

class RankingScreen(Screen):
    
    # Define una propiedad para la fuente de la imagen
    image_source = StringProperty("../../image/monkeys/happy.png")  # Imagen inicial estática
    image_text = StringProperty("The monkey is happy!")  # Texto inicial estático

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def incrementar_nota(self):
        # La función no cambia la imagen ni el texto, solo está aquí por si se necesita algún comportamiento adicional
        pass
