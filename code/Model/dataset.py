import pandas as pd
import numpy as np

submision = pd.read_csv("./../../data/trameses.csv")

submision['grade'] = submision['grade'].fillna(-1)
submision = submision.sort_values(by=['userid', 'activitat_id', 'datesubmitted'])
submision['attempt_number'] = submision.groupby(['userid', 'activitat_id']).cumcount() + 1
submision = submision.sort_values(by=['userid', 'activitat_id', 'grade', 'dategraded'], ascending=[True, True, False, True])
submision = submision.drop_duplicates(subset=['userid', 'activitat_id'], keep='first')

activities = pd.read_csv("./../../data/activitats.csv", encoding='ISO-8859-1')

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
submision_activities_marks["datesubmitted"] = pd.to_datetime(submision_activities_marks['datesubmitted'], unit='s')
submision_activities_marks["dategraded"] = pd.to_datetime(submision_activities_marks['dategraded'], unit='s')
submision_activities_marks["startdate"] = pd.to_datetime(submision_activities_marks['startdate'], unit='s')
submision_activities_marks["duedate"] = pd.to_datetime(submision_activities_marks['duedate'], unit='s')
submision_activities_marks['rank_P'] = submision_activities_marks.groupby('aula_id')['P_Grade'].rank(method='dense', ascending=False)
submision_activities_marks['rank_F'] = submision_activities_marks.groupby('aula_id')['F_Grade'].rank(method='dense', ascending=False)
submision_activities_marks['rank_R'] = submision_activities_marks.groupby('aula_id')['R_Grade'].rank(method='dense', ascending=False)

dataset = submision_activities_marks[["userid", "aula_id", "activitat_id", "activitat", "startdate", "duedate", "datesubmitted", "dategraded", "attempt_number", "mark", "NOT_Presented_P", "P_Grade", "P_Grade_Date", "NOT_Presented_F", "F_Grade", "F_Grade_Date", "NOT_Presented_R", "R_Grade", "R_Grade_Date"]]

dataset.to_csv('./../../data/dataset.csv', index=False)
