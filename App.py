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
#esborrar
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

# Definim les pantalles individuals

class MainScreen(Screen):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        # Botó per a Ranking
        ranking_button = Button(text="Ranking", font_size='20sp')
        ranking_button.bind(on_press=self.go_to_ranking)
        layout.add_widget(ranking_button)

        # Botó per a Statistics
        statistics_button = Button(text="Statistics", font_size='20sp')
        statistics_button.bind(on_press=self.go_to_statistics)
        layout.add_widget(statistics_button)

        # Botó per a Predictions
        predictions_button = Button(text="Predictions", font_size='20sp')
        predictions_button.bind(on_press=self.go_to_predictions)
        layout.add_widget(predictions_button)

        # Botó per a Reinforcement Activities
        reinforcement_button = Button(text="Reinforcement Activities", font_size='20sp')
        reinforcement_button.bind(on_press=self.go_to_reinforcement)
        layout.add_widget(reinforcement_button)

        self.add_widget(layout)

    def go_to_ranking(self, instance):
        self.manager.current = 'ranking'

    def go_to_statistics(self, instance):
        self.manager.current = 'statistics'

    def go_to_predictions(self, instance):
        self.manager.current = 'predictions'

    def go_to_reinforcement(self, instance):
        self.manager.current = 'reinforcement_activities'


class RankingScreen(Screen):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        label = Label(text="Ranking Screen", font_size='24sp')
        layout.add_widget(label)
        back_button = Button(text="Back", size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5})
        back_button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)
        self.add_widget(layout)


class StatisticsScreen(Screen):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        label = Label(text="Statistics Screen", font_size='24sp')
        layout.add_widget(label)
        back_button = Button(text="Back", size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5})
        back_button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)
        self.add_widget(layout)


class PredictionsScreen(Screen):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        label = Label(text="Predictions Screen", font_size='24sp')
        layout.add_widget(label)
        back_button = Button(text="Back", size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5})
        back_button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)
        self.add_widget(layout)


class ReinforcementActivitiesScreen(Screen):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20)
        label = Label(text="Reinforcement Activities Screen", font_size='24sp')
        layout.add_widget(label)
        back_button = Button(text="Back", size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5})
        back_button.bind(on_press=lambda instance: setattr(self.manager, 'current', 'main'))
        layout.add_widget(back_button)
        self.add_widget(layout)


# Classe de l'aplicació principal

class MyApp(App):
    def build(self):
        # Creamos el ScreenManager y añadimos todas las pantallas
        sm = ScreenManager()

        main_screen = MainScreen(name='main')
        ranking_screen = RankingScreen(name='ranking')
        statistics_screen = StatisticsScreen(name='statistics')
        predictions_screen = PredictionsScreen(name='predictions')
        reinforcement_activities_screen = ReinforcementActivitiesScreen(name='reinforcement_activities')

        for screen in [main_screen, ranking_screen, statistics_screen, predictions_screen, reinforcement_activities_screen]:
            screen.build()
            sm.add_widget(screen)

        return sm

if __name__ == '__main__':
    MyApp().run()
