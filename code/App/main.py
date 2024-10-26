# import llista_nota from algun_lloc
# import recomanacions from algun_lloc
#esborrar

recomanacions = {}

llista_nota = {
  12: 4.5,
  13: 5.5,
  14: 6.5,
  15: 7.32
}

llista_assigs = {
  12: "Mates",
  13: "Llengua",
  14: "Anglès",
  15: "Tecnologia"
}

from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from code.App.Screens.HomeScreen import HomeScreen
from code.App.Screens.RankingScreen import RankingScreen
from code.App.Screens.StatisticsScreen import StatisticsScreen
from code.App.Screens.PredictionsScreen import PredictionsScreen
from code.App.Screens.ReinforcementActivitiesScreen import ReinforcementActivitiesScreen

class MainApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Brown"
        return Builder.load_file("./main.kv")

    def menu_callback(self, screen_name):
        # Canvia a la pantalla seleccionada
        self.root.ids.screen_manager.current = screen_name
        # Tanca el menú després de seleccionar una opció
        self.root.ids.nav_drawer.set_state("close")

if __name__ == '__main__':
    MainApp().run()
