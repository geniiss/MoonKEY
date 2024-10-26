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
from kivy.uix.label import Label

Builder.load_file("kv_files/StatisticsScreen.kv")

class StatisticsScreen(Screen):
    def on_enter(self, *args):
        # Generem el gràfic amb la funció pie_chart
        plt_figure = pie_chart(155)
        
        # Convertim el gràfic en una imatge per ser mostrada en Kivy
        self.update_chart(plt_figure)
        
    def update_chart(self, plt_figure):
        # Guardem el gràfic com a imatge temporal
        canvas = FigureCanvas(plt_figure.gcf())
        canvas.draw()
        texture = Texture.create(size=(int(canvas.get_width_height()[0]), int(canvas.get_width_height()[1])), colorfmt='rgba')
        texture.blit_buffer(canvas.tostring_argb(), colorfmt='argb', bufferfmt='ubyte')
        texture.flip_vertical()
        
        # Eliminar els elements anteriors a `chart_box`
        self.ids.chart_box.clear_widgets()
        
        # Crear una imatge a partir de la textura i afegir-la a la interfície
        img = Image(texture=texture)
        self.ids.chart_box.add_widget(img)
        
        # Afegir un títol a la imatge
        # Add the title label to the chart_box
        title_label = Label(text="Títol del Gràfic", size_hint_y=None, height=40)
        self.ids.chart_box.add_widget(title_label)
        
        # Ajustar la posició dels elements per fer que es vegin més baixos
        for widget in self.ids.chart_box.children:
            widget.y -= 100  # Ajustar aquest valor segons sigui necessari
