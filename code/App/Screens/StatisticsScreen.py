from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import sys
import os
import matplotlib.pyplot as plt
from kivymd.uix.list import OneLineListItem
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from Screens.SubjectScreen import SubjectScreen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Model')))
from pie_chart import pie_chart

Builder.load_file("kv_files/StatisticsScreen.kv")

# Llista de codis d'assignatures
llista_assigs = [12, 13, 14, 15]

class StatisticsScreen(Screen):
    def on_enter(self, *args):
        # Establim els valors de les mitjanes directament des del codi
        self.ids.final_grade_avg.text = "6.3"
        self.ids.activity_grade_avg.text = "8.3"

        # Generem el gràfic amb la funció pie_chart
        plt_figure = pie_chart(155)
        self.update_chart(plt_figure)

        # Afegim els codis d'assignatures a la llista scrollejable
        self.populate_subjects_list()
        
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
    
    def populate_subjects_list(self):
        # Afegim els elements de la llista d'assignatures
        for code in llista_assigs:
            item = OneLineListItem(text=f"Subject Code: {code}")
            item.bind(on_release=lambda x, code=code: self.open_subject_screen(code))
            self.ids.subjects_list.add_widget(item)

    def open_subject_screen(self, code):
        # Obre una nova pantalla per a l'assignatura seleccionada
        subject_screen = SubjectScreen(name=f"subject_{code}")
        subject_screen.subject_code = str(code)
        self.manager.add_widget(subject_screen)
        self.manager.current = subject_screen.name
