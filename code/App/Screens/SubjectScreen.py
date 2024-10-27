# SubjectScreen.py

from kivy.uix.screenmanager import Screen
from kivy.graphics.texture import Texture
from kivy.lang import Builder
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import sys
import os
from kivy.uix.image import Image
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Model')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from user_login import user_id
from Statistic_Tables import submition_temporal_graph, pie_chart_submissions_user_aula

Builder.load_file("kv_files/SubjectScreen.kv")

class SubjectScreen(Screen):
    def __init__(self, aula_id, **kwargs):
        super(SubjectScreen, self).__init__(**kwargs)
        self.aula_id = aula_id  # Emmagatzema l'aula_id com a atribut de la classe

    def on_enter(self, *args):
        # Aquí podríem utilitzar self.aula_id per recuperar dades específiques d'aquesta assignatura
        # Per exemple, carregar un gràfic o estadístiques basades en l'aula_id
        self.update_pie_chart()
        self.update_line_chart()

    def update_pie_chart(self):
        # Genera el gràfic circular amb matplotlib basat en l'aula_id
        fig = pie_chart_submissions_user_aula(user_id, self.aula_id)  # Suposem que pie_chart() rep l'aula_id com a paràmetre
        canvas = FigureCanvas(fig.gcf())
        canvas.draw()

        width, height = canvas.get_width_height()
        texture = Texture.create(size=(width, height), colorfmt='rgba')
        texture.blit_buffer(canvas.tostring_rgb(), colorfmt='rgb', bufferfmt='ubyte')

        self.ids.pie_chart_box.clear_widgets()
        
        texture.flip_vertical()
        img = Image(texture=texture)

        self.ids.pie_chart_box.add_widget(img)

    def update_line_chart(self):
        # Genera el gràfic de línies basat en l'aula_id
        fig = submition_temporal_graph(user_id, self.aula_id)  # Suposem que aquesta funció rep l'aula_id
        canvas = FigureCanvas(fig.gcf())
        canvas.draw()
        width, height = canvas.get_width_height()
        texture = Texture.create(size=(width, height), colorfmt='rgba')
        texture.blit_buffer(canvas.tostring_rgb(), colorfmt='rgb', bufferfmt='ubyte')
        texture.flip_vertical()
        self.ids.line_chart_box.clear_widgets()
        img = Image(texture=texture)
        self.ids.line_chart_box.add_widget(img)
