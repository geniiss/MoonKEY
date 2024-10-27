import sys
import os
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty

Builder.load_file("kv_files/HomeScreen.kv")

from user_login import user_id
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Model')))
from Statistic_Tables import stats_Academic_Record_Mean_Final_Grade


# Enum de las diferentes calificaciones posibles
FAILED = 1
PASSED = 2
GOOD = 3
EXCELENT = 4
ERROR = -1
calification = {4:"EXCELENT", 3:"GOOD", 2:"PASSED", 1:"FAILED"}

# Pasa de una nota del 0.0 al 10.0 a una nota categórica
def numeric_grade_to_grade(grade):
    match grade:
        case grade if 0 <= grade < 5:
            return FAILED
        case grade if 5 <= grade < 7:
            return PASSED
        case grade if 7 <= grade < 9:
            return GOOD
        case grade if 9 <= grade <= 10:
            return EXCELENT
        case _:
            return ERROR

class HomeScreen(Screen):
    # Define una propiedad para la fuente de la imagen
    image_source = StringProperty("")
    image_text = StringProperty("")  # Define el texto para esta imagen inicial
    nota = NumericProperty()  # Variable para almacenar la nota

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.nota = float(stats_Academic_Record_Mean_Final_Grade(user_id))
        self.set_image(numeric_grade_to_grade(self.nota))

    def set_image(self, nota):
        # Cambia la fuente de la imagen según el valor de la variable
        self.image_text = calification[numeric_grade_to_grade(self.nota)] + "\n"

        if nota == EXCELENT:
            self.image_source = "../../image/monkeys/happy.png"
            self.image_text += "Really good, you got the max mark!"
        elif nota == GOOD:
            self.image_source = "../../image/monkeys/smile.png"
            self.image_text += "Good, keep it going!"
        elif nota == PASSED:
            self.image_source = "../../image/monkeys/sad2.png"
            self.image_text += "A bit tight :/"
        elif nota == FAILED:
            self.image_source = "../../image/monkeys/angry2.png"
            self.image_text += "Oh no, the moonkey got mad :O"
        else:
            print("Error")