from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import sys
import os
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Model')))
from pie_chart import pie_chart
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

Builder.load_file("kv_files/StatisticsScreen.kv")

class StatisticsScreen(Screen):
    def on_enter(self, *args):
        # Establim els valors de les mitjanes directament des del codi
        self.ids.final_grade_avg.text = "6.3"  # Actualitza el valor del label de final_grade_avg
        self.ids.activity_grade_avg.text = "8.3"  # Actualitza el valor del label de activity_grade_avg

        # Generem el gràfic amb la funció pie_chart
        plt_figure = pie_chart(155)
        
        # Convertim el gràfic en una imatge per ser mostrada en Kivy
        self.update_chart(plt_figure)
        
    def update_chart(self, plt_figure):
        # Dibuixem la figura en el canvas
        canvas = FigureCanvas(plt_figure.gcf())
        canvas.draw()
        
        # Cream una textura a partir del gràfic
        width, height = canvas.get_width_height()
        texture = Texture.create(size=(width, height), colorfmt='rgba')
        texture.blit_buffer(canvas.tostring_argb(), colorfmt='argb', bufferfmt='ubyte')
        texture.flip_vertical()
        
        # Esborrem els widgets anteriors de `chart_box`
        self.ids.chart_box.clear_widgets()
        
        # Afegim la imatge del gràfic a `chart_box`
        img = Image(texture=texture)
        self.ids.chart_box.add_widget(img)
