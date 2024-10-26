from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty

Builder.load_file("kv_files/HomeScreen.kv")
class HomeScreen(Screen):
    # Define una propiedad para la fuente de la imagen
    image_source = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_image(2)  # Llama a la función para establecer la imagen inicial

    def set_image(self, imagen):
        # Cambia la fuente de la imagen según el valor de la variable
        if imagen == 1:
            self.image_source = "../../image/monkeys/happy.png"
        elif imagen == 2:
            self.image_source = "../../image/monkeys/sad.png"
        elif imagen == 3:
            self.image_source = "../../image/monkeys/angry.png"
        # Puedes añadir más condiciones según tus necesidades
