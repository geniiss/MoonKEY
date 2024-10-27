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
        self.aula_id = aula_id  # Store aula_id as a class attribute

    def on_enter(self, *args):
        # Update charts when the screen is displayed
        self.update_pie_chart()
        self.update_line_chart()
        self.update_activity_chart()

    def update_pie_chart(self):
        # Generate and display the main pie chart
        fig = pie_chart_submissions_user_aula(user_id, self.aula_id)
        canvas = FigureCanvas(fig)
        canvas.draw()
        
        width, height = canvas.get_width_height()
        texture = Texture.create(size=(width, height), colorfmt='rgba')
        texture.blit_buffer(canvas.tostring_rgb(), colorfmt='rgb', bufferfmt='ubyte')
        texture.flip_vertical()

        self.ids.pie_chart_box.clear_widgets()
        img = Image(texture=texture)
        self.ids.pie_chart_box.add_widget(img)

    def update_activity_chart(self):
        # Generate a secondary pie chart for activity grades (mock data)
        fig, ax = plt.subplots()
        ax.pie([30, 40, 30], labels=["Activity 1", "Activity 2", "Activity 3"], autopct='%1.1f%%')
        
        canvas = FigureCanvas(fig)
        canvas.draw()

        width, height = canvas.get_width_height()
        texture = Texture.create(size=(width, height), colorfmt='rgba')
        texture.blit_buffer(canvas.tostring_rgb(), colorfmt='rgb', bufferfmt='ubyte')
        texture.flip_vertical()

        self.ids.activity_chart_box.clear_widgets()
        img = Image(texture=texture)
        self.ids.activity_chart_box.add_widget(img)

    def update_line_chart(self):
        # Generate and display the line chart
        fig = submition_temporal_graph(user_id, self.aula_id)
        canvas = FigureCanvas(fig)
        canvas.draw()
        
        width, height = canvas.get_width_height()
        texture = Texture.create(size=(width, height), colorfmt='rgba')
        texture.blit_buffer(canvas.tostring_rgb(), colorfmt='rgb', bufferfmt='ubyte')
        texture.flip_vertical()

        self.ids.line_chart_box.clear_widgets()
        img = Image(texture=texture)
        self.ids.line_chart_box.add_widget(img)
