from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
import sys
import os
import matplotlib.pyplot as plt
from kivymd.uix.list import OneLineListItem
from kivymd.uix.datatables import MDDataTable
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from Screens.SubjectScreen import SubjectScreen
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Model')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from user_login import user_id
from pie_chart import pie_chart
from Statistic_Tables import Academic_Record, stats_Academic_Record_Mean_Final_Grade, stats_Academic_Record_Mean_Marks

Builder.load_file("kv_files/StatisticsScreen.kv")

# Llista de codis d'assignatures
academic_record = Academic_Record(user_id)
# Ex: academic_record = [['aula_id', 'Nota_Final', 'Fecha_Final'], [12, '7.5', '2024-06-10']]

class StatisticsScreen(Screen):
    def on_enter(self, *args):
        # Establim els valors de les mitjanes directament des del codi
        self.ids.final_grade_avg.text = f'{stats_Academic_Record_Mean_Final_Grade(user_id):.2f}'
        self.ids.activity_grade_avg.text = f'{stats_Academic_Record_Mean_Marks(user_id):.2f}'

        # Generem el gràfic amb la funció pie_chart
        plt_figure = pie_chart(user_id)
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
    # Itera sobre cada asignatura en academic_record
        self.ids.subjects_list.clear_widgets()
        for i in range(len(academic_record['aula_id'])):
            aula_id = academic_record['aula_id'].values[i]
            nota_final = academic_record['Nota_Final'].values[i]
            fecha_final = academic_record['Fecha_Final'].values[i]
            # [aula_id, nota_final, fecha_final] = subject
            # Crea un elemento de lista con el aula_id como texto y añade la función para abrir la pantalla correspondiente
            item = OneLineListItem(text=f"              Subject: {aula_id}                Grade: {nota_final}", 
                                    on_release=lambda x, aula_id=aula_id: self.open_subject_screen(aula_id))
            # Añade el item a la lista de subjects_list en el archivo kv
            self.ids.subjects_list.add_widget(item)


    def open_subject_screen(self, code):
        # Obre una nova pantalla per a l'assignatura seleccionada
        subject_screen = SubjectScreen(name=f"subject_{code}")
        subject_screen.subject_code = str(code)
        self.manager.add_widget(subject_screen)
        self.manager.current = subject_screen.name

