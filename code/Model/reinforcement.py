import openai
import pandas as pd
from api_key import KEY

openai.api_key = KEY

def reinforcment_advice(dataset, user_id):
    dataset = dataset[dataset["userid"] == user_id]
    dataset = dataset[dataset["userid"] == user_id]
    dataset["is_worst_activity"] = dataset.groupby("aula_id")["activitat"].transform(lambda x: x == x.min())
    dataset = dataset[dataset["is_worst_activity"] == True]
    dataset[["aula_id", "P_Grade", "F_Grade", "R_Grade", "activitat", "mark"]]
    dataset = dataset.rename(columns={
        'aula_id': 'Subject',
        'activitat': 'Activity_Name',
        'mark': 'Activity_Grade'
    })
    dataset = dataset[["Subject", "P_Grade", "F_Grade", "R_Grade", "Activity_Name", "Activity_Grade"]]
    table = dataset.to_string(max_rows=None, max_cols=None)
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a virtual assistant providing academic reinforcement advice. Your role is, based on a data table containing the Subject, grades from the midterm exam, final exam, and retake (P_Grade, F_Grade, R_Grade), as well as all activities (Activity) and their grades (Activity_Grade), to decide which subject requires reinforcement and recommend three points for improvement."},
            {"role": "user", "content": table}
        ]
    )
    return response.choices[0].message["content"]

    

