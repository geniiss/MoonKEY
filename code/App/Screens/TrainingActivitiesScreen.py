from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Model')))
from reinforcement import reinforcment_advice
import pandas as pd

Builder.load_file("kv_files/TrainingActivitiesScreen.kv")
dataset = pd.read_csv('./../../data/dataset.csv')

class TrainingActivitiesScreen(Screen):
    card_text = StringProperty(reinforcment_advice(dataset, 789))  

    def update_text(self, new_text):
        self.card_text = new_text  