from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Model')))
from Statistic_Tables import ranking_user

Builder.load_file("kv_files/RankingScreen.kv")
class RankingScreen(Screen):
    user_id = 155  # Variable user_id hardcodeada

    # Define propiedades para la fuente de la imagen y el texto
    image_source = StringProperty("../../image/monkeys/ranking.png")  # Imagen inicial estática
    image_text = StringProperty("")  # Texto inicial vacío que se actualizará

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_ranking()  # Llama a la función para obtener el ranking en la inicialización

    def update_ranking(self):
        # Obtiene el ranking del usuario y actualiza el texto
        ranking = ranking_user(self.user_id)  # Llama a la función ranking_user
        self.image_text = f"You're #{ranking} among all students!! Congrats!!!"  # Actualiza el texto

    def get_ranking_number(self):
        # Devuelve solo el número del ranking
        return self.image_text.split('#')[1].split()[0]  # Extrae solo el número

