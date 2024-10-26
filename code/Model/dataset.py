import pandas as pd
import numpy as np

submision = pd.read_csv("./../../data/trameses.csv")

submision['grade'] = submision['grade'].fillna(-1)
submision = submision.sort_values(by=['userid', 'activitat_id', 'datesubmitted'])
submision['attempt_number'] = submision.groupby(['userid', 'activitat_id']).cumcount() + 1
submision = submision.sort_values(by=['userid', 'activitat_id', 'grade', 'dategraded'], ascending=[True, True, False, True])
submision = submision.drop_duplicates(subset=['userid', 'activitat_id'], keep='first')
submision['grade'] = submision['grade'].replace(-1, 0)

activities = pd.read_csv("./../../data/activitats.csv", encoding='ISO-8859-1')
activities["count_activities"] = activities.groupby('aula_id')['activitat_id'].transform('count')

submision_activities = submision.merge(activities, on=['activitat_id'], how='left')
submision_activities["mark"] = submision_activities["grade_x"].astype(float) / submision_activities["grade_y"].astype(float)

marks = pd.read_csv("./../../data/notes.csv", delimiter=';')

submision_activities_marks = marks.merge(submision_activities, on=['userid','aula_id'], how='left')
submision_activities_marks["NOT_Presented_P"] = np.where(submision_activities_marks['P_Grade_Date'].notnull() & submision_activities_marks['P_Grade'].isnull(), 1, 0)
submision_activities_marks["NOT_Presented_F"] = np.where(submision_activities_marks['F_Grade_Date'].notnull() & submision_activities_marks['F_Grade'].isnull(), 1, 0)
submision_activities_marks["NOT_Presented_R"] = np.where(submision_activities_marks['R_Grade_Date'].notnull() & submision_activities_marks['R_Grade'].isnull(), 1, 0)
submision_activities_marks["P_Grade_Date"] = pd.to_datetime(submision_activities_marks['P_Grade_Date'], unit='s')
submision_activities_marks["F_Grade_Date"] = pd.to_datetime(submision_activities_marks['F_Grade_Date'], unit='s')
submision_activities_marks["R_Grade_Date"] = pd.to_datetime(submision_activities_marks['R_Grade_Date'], unit='s')
submision_activities_marks['Nota_Final'] = np.where(submision_activities_marks['R_Grade'].notna(), submision_activities_marks['R_Grade'], submision_activities_marks['F_Grade'])
submision_activities_marks["datesubmitted"] = pd.to_datetime(submision_activities_marks['datesubmitted'], unit='s')
submision_activities_marks["dategraded"] = pd.to_datetime(submision_activities_marks['dategraded'], unit='s')
submision_activities_marks["startdate"] = pd.to_datetime(submision_activities_marks['startdate'], unit='s')
submision_activities_marks["duedate"] = pd.to_datetime(submision_activities_marks['duedate'], unit='s')
submision_activities_marks['rank_P'] = submision_activities_marks.groupby('aula_id')['P_Grade'].rank(method='dense', ascending=False)
submision_activities_marks['rank_F'] = submision_activities_marks.groupby('aula_id')['F_Grade'].rank(method='dense', ascending=False)
submision_activities_marks['rank_R'] = submision_activities_marks.groupby('aula_id')['R_Grade'].rank(method='dense', ascending=False)
submision_activities_marks['rank_FG'] = submision_activities_marks.groupby('aula_id')['Nota_Final'].rank(method='dense', ascending=False)
submision_activities_marks["P_Grade"] = submision_activities_marks["P_Grade"].str.replace(',', '.', regex=False).astype(float)
submision_activities_marks["F_Grade"] = submision_activities_marks["F_Grade"].str.replace(',', '.', regex=False).astype(float)
submision_activities_marks["R_Grade"] = submision_activities_marks["R_Grade"].str.replace(',', '.', regex=False).astype(float)


dataset = submision_activities_marks[["userid", "aula_id", "activitat_id", "activitat", "startdate", "duedate", "datesubmitted", "dategraded", "attempt_number", "mark", "NOT_Presented_P", "P_Grade", "P_Grade_Date", "NOT_Presented_F", "F_Grade", "F_Grade_Date", "NOT_Presented_R", "R_Grade", "R_Grade_Date", "rank_P", "rank_F", "rank_R", "count_activities", "Nota_Final", "rank_FG"]]


dataset = dataset.astype({
    "userid": "int64",                # ID de usuario (número entero)
    "aula_id": "int64",               # ID del aula (número entero)
    "activitat_id": "Int64",          # ID de la actividad (entero que permite valores NaN)
    "activitat": "string",            # Nombre de la actividad (texto)
    "startdate": "datetime64[ns]",        # Fecha de inicio (fecha)
    "duedate": "datetime64[ns]",          # Fecha de vencimiento (fecha)
    "datesubmitted": "datetime64[ns]",    # Fecha de entrega (fecha)
    "dategraded": "datetime64[ns]",       # Fecha de evaluación (fecha)
    "attempt_number": "Int64",        # Número de intento (entero que permite NaN)
    "mark": "float64",                # Calificación (decimal)
    "NOT_Presented_P": "int64",       # Indicador de no presentación (P, entero)
    "P_Grade": "float",              # Grado P (texto)
    "P_Grade_Date": "datetime64[ns]",     # Fecha de grado P (fecha)
    "NOT_Presented_F": "int64",       # Indicador de no presentación (F, entero)
    "F_Grade": "float",              # Grado F (texto)
    "F_Grade_Date": "datetime64[ns]",     # Fecha de grado F (fecha)
    "NOT_Presented_R": "int64",       # Indicador de no presentación (R, entero)
    "R_Grade": "float",              # Grado R (texto)
    "R_Grade_Date": "datetime64[ns]",     # Fecha de grado R (fecha)
    "rank_P": "Int64",              # Ranking P (decimal)
    "rank_F": "Int64",              # Ranking F (decimal)
    "rank_R": "Int64",              # Ranking R (decimal)
    "count_activities": "Int64"
})
print(dataset)

dataset.to_csv('./../../data/dataset.csv', index=False)

