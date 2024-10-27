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
from models import prediction_model
Builder.load_file("kv_files/SubjectScreen.kv")

class SubjectScreen(Screen):
    def __init__(self, aula_id, **kwargs):
        super(SubjectScreen, self).__init__(**kwargs)
        self.aula_id = aula_id  # Store aula_id as a class attribute

    def on_enter(self, *args):
        # Update charts when the screen is displayed
        self.update_pie_chart()
        self.update_line_chart()
        F, R = prediction_model('./../../data/models/model_141_P.pkl', './../../data/models/model_141_R.pkl', user_id, self.aula_id)
        self.ids.estimated_recovery_grade.text = f'{R:.2f}'
        self.ids.estimated_final_grade.text = f'{F:.2f}'

    def update_pie_chart(self):
        # Generate and display the main pie chart
        fig = pie_chart_submissions_user_aula(user_id, self.aula_id)
        canvas = FigureCanvas(fig.gcf())
        canvas.draw()
        
        width, height = canvas.get_width_height()
        texture = Texture.create(size=(width, height), colorfmt='rgba')
        texture.blit_buffer(canvas.tostring_rgb(), colorfmt='rgb', bufferfmt='ubyte')
        texture.flip_vertical()

        self.ids.pie_chart_box.clear_widgets()
        img = Image(texture=texture)
        self.ids.pie_chart_box.add_widget(img)

    def update_line_chart(self):
        # Generate and display the line chart
        fig = submition_temporal_graph(user_id, self.aula_id)
        canvas = FigureCanvas(fig.gcf())
        canvas.draw()
        
        width, height = canvas.get_width_height()
        texture = Texture.create(size=(width, height), colorfmt='rgba')
        texture.blit_buffer(canvas.tostring_rgb(), colorfmt='rgb', bufferfmt='ubyte')
        texture.flip_vertical()

        self.ids.line_chart_box.clear_widgets()
        img = Image(texture=texture)
        self.ids.line_chart_box.add_widget(img)
