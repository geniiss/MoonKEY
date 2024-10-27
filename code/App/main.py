from kivy.config import Config
Config.read('config.ini')  # Cargar la configuración antes de importar otros módulos

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.core.text import LabelBase

from Screens.HomeScreen import HomeScreen
from Screens.RankingScreen import RankingScreen
from Screens.StatisticsScreen import StatisticsScreen
from Screens.TrainingActivitiesScreen import TrainingActivitiesScreen



Header = {
    "home": "MoonKEY",
    "ranking": "Ranking",
    "statistics": "Statistics",
    "training_activities": "Training Activities"
}

class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Brown"
        return Builder.load_file("./main.kv")
        
    def delete_styles(self):
        self.root.ids.home_item.font_style = "Body1";
        self.root.ids.ranking_item.font_style = "Body1";
        self.root.ids.statistics_item.font_style = "Body1";
        self.root.ids.training_activities_item.font_style = "Body1";
    
    def menu_callback(self, screen_name):
        # Restablecer todos los estilos a 'Body1'
        self.delete_styles()

        # Solo aplica el estilo 'H6' al elemento seleccionado
        if screen_name == "home":
            self.root.ids.home_item.font_style = "H6"
        elif screen_name == "ranking":
            self.root.ids.ranking_item.font_style = "H6"
        elif screen_name == "statistics":
            self.root.ids.statistics_item.font_style = "H6"
        elif screen_name == "training_activities":
            self.root.ids.training_activities_item.font_style = "H6"

        # Cambia a la pantalla seleccionada
        self.root.ids.top_bar.title = Header[screen_name]
        self.root.ids.screen_manager.current = screen_name
        # Cierra el menú después de seleccionar una opción
        self.root.ids.nav_drawer.set_state("close")

if __name__ == '__main__':
    MainApp().run()