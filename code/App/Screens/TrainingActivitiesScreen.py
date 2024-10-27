from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'Model')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from reinforcement import reinforcment_advice
import pandas as pd
from user_login import user_id

Builder.load_file("kv_files/TrainingActivitiesScreen.kv")
dataset = pd.read_csv('./../../data/dataset.csv')

class TrainingActivitiesScreen(Screen):
    card_text = StringProperty("Analyzing your weaknesses...")

    def on_enter(self):
        self.card_text = reinforcment_advice(dataset, user_id)