from kivy.config import Config
Config.read('config.ini')  # Cargar la configuración antes de importar otros módulos

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from Screens.HomeScreen import HomeScreen
from Screens.RankingScreen import RankingScreen
from Screens.StatisticsScreen import StatisticsScreen
from Screens.PredictionsScreen import PredictionsScreen
from Screens.ReinforcementActivitiesScreen import ReinforcementActivitiesScreen

Header = {
    "home": "MoonKEY",
    "ranking": "Ranking",
    "statistics": "Statistics",
    "predictions": "Predictions",
    "reinforcement_activities": "Reinforcement Activities"
}
class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Brown"
        return Builder.load_file("./main.kv")

    def menu_callback(self, screen_name):
        # Cambia a la pantalla seleccionada
        self.root.ids.top_bar.title = Header[screen_name]
        self.root.ids.screen_manager.current = screen_name
        # Cierra el menú después de seleccionar una opción
        self.root.ids.nav_drawer.set_state("close")

if __name__ == '__main__':
    MainApp().run()