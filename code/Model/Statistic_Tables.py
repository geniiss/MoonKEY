import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def Academic_Record_user_aula(user_id, aula_id):
    activities = pd.read_csv("./../../data/activitats.csv", encoding='ISO-8859-1')
    marks = pd.read_csv("./../../data/notes.csv", delimiter=';')
    submision = pd.read_csv("./../../data/trameses.csv")

    marks_user = marks[(marks["userid"] == user_id)]
    marks_user = marks_user[marks_user["aula_id"] == aula_id]
    marks_user = marks_user[["userid", "aula_id", "P_Grade", "F_Grade", "R_Grade"]]


    return marks_user

def Academic_Record(user_id):

    activities = pd.read_csv("./../../data/activitats.csv", encoding='ISO-8859-1')
    marks = pd.read_csv("./../../data/notes.csv", delimiter=';')
    submision = pd.read_csv("./../../data/trameses.csv")

    marks_user = marks[(marks["userid"] == user_id)]

    #Transforma los formatos de fecha UNIX
    marks_user.loc[:,'P_Grade_Date'] = pd.to_datetime(marks_user.loc[:,'P_Grade_Date'], unit='s').dt.date
    marks_user.loc[:,'F_Grade_Date'] = pd.to_datetime(marks_user.loc[:,'F_Grade_Date'], unit='s').dt.date
    marks_user.loc[:,'R_Grade_Date'] = pd.to_datetime(marks_user.loc[:,'R_Grade_Date'], unit='s').dt.date

    #Obtiene la nota y fecha de convocatoria finales (se actualiza la nota final en caso de hacerse recuperacion)
    marks_user['Nota_Final'] = np.where(marks_user['R_Grade'].notna(), marks_user['R_Grade'], marks_user['F_Grade'])
    marks_user['Fecha_Final'] = np.where(marks_user['R_Grade'].notna(), marks_user['R_Grade_Date'], marks_user['F_Grade_Date'])

    #Filtra los campos finales
    marks_user_record = marks_user[["aula_id", "Nota_Final", "Fecha_Final"]]

    return marks_user_record



def Academic_Record_Subject(user_id, aula_id):
    activities = pd.read_csv("./../../data/activitats.csv", encoding='ISO-8859-1')
    marks = pd.read_csv("./../../data/notes.csv", delimiter=';')
    submision = pd.read_csv("./../../data/trameses.csv")

    marks_user = marks[(marks["userid"] == user_id)]

    #Transforma los formatos de fecha UNIX
    marks_user.loc[:,'P_Grade_Date'] = pd.to_datetime(marks_user.loc[:,'P_Grade_Date'], unit='s').dt.date
    marks_user.loc[:,'F_Grade_Date'] = pd.to_datetime(marks_user.loc[:,'F_Grade_Date'], unit='s').dt.date
    marks_user.loc[:,'R_Grade_Date'] = pd.to_datetime(marks_user.loc[:,'R_Grade_Date'], unit='s').dt.date

    return marks_user[marks["aula_id"] == aula_id]



def pie_chart_submissions_user(user_id):
    fontsize = 18
    submissions = pd.read_csv("./../../data/dataset.csv")
    submissions = submissions[['userid', 'aula_id', 'activitat', "activitat_id", 'datesubmitted', 'attempt_number', 'mark', 'count_activities']]

    submissions_user = submissions[submissions["userid"] == user_id]

    conteo_por_aula = submissions_user.groupby('aula_id').size()
    conteo_por_aula = conteo_por_aula.rename('conteo_registros').reset_index()
    submissions_user = submissions_user.merge(conteo_por_aula, on='aula_id', how='left')
    submissions_user['diferencia'] = submissions_user['count_activities'] - submissions_user['conteo_registros']

    conteo_por_aula = submissions_user.groupby('aula_id').size()
    conteo_por_aula = conteo_por_aula.rename('conteo_registros').reset_index()

    if 'conteo_registros' in submissions_user.columns:
        submissions_user = submissions_user.drop(columns=['conteo_registros'])

    submissions_user = submissions_user.merge(conteo_por_aula, on='aula_id', how='left')
    submissions_user['diferencia'] = submissions_user['count_activities'] - submissions_user['conteo_registros']

    suma_valores_distintos = submissions_user['diferencia'].unique().sum()

    count_mark_1 = (submissions_user['mark'] == 1).sum()
    count_mark_0 = (submissions_user['mark'] == 0).sum()
    count_between_0_and_1 = ((submissions_user['mark'] > 0) & (submissions_user['mark'] < 1)).sum()

    sizes = [count_mark_1, count_between_0_and_1, count_mark_0, suma_valores_distintos]
    labels = ['10', 'Other', '0', 'NaN']
    colors = ['#8BC34A', '#FFC107', '#FF4C4C', '#696969']  # Verde, rojo, amarillo, gris oscuro (DimGray)

    # Crear el gráfico circular con ajustes para evitar superposición
    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        textprops={'fontsize': fontsize},
        labeldistance=1.1,      # Alejar las etiquetas del centro
        pctdistance=.7  # Ajustar la posición de los porcentajes
    )

    plt.axis('equal')

    
    return plt






def pie_chart_submissions_user_aula(user_id, aula_id):
    fontsize = 24
    submissions = pd.read_csv("./../../data/dataset.csv")
    submissions = submissions[['userid', 'aula_id', 'activitat', "activitat_id", 'datesubmitted', 'attempt_number', 'mark', 'count_activities']]

    submissions_user = submissions[submissions["userid"] == user_id]
    submissions_user = submissions_user[submissions_user["aula_id"] == aula_id]

    conteo_por_aula = submissions_user.groupby('aula_id').size()
    conteo_por_aula = conteo_por_aula.rename('conteo_registros').reset_index()
    submissions_user = submissions_user.merge(conteo_por_aula, on='aula_id', how='left')
    submissions_user['diferencia'] = submissions_user['count_activities'] - submissions_user['conteo_registros']

    # Paso 2: Contar registros por aula_id y agregarlo como columna 'conteo_registros'
    conteo_por_aula = submissions_user.groupby('aula_id').size()
    conteo_por_aula = conteo_por_aula.rename('conteo_registros').reset_index()

    if 'conteo_registros' in submissions_user.columns:
        submissions_user = submissions_user.drop(columns=['conteo_registros'])

    submissions_user = submissions_user.merge(conteo_por_aula, on='aula_id', how='left')
    submissions_user['diferencia'] = submissions_user['count_activities'] - submissions_user['conteo_registros']

    suma_valores_distintos = submissions_user['diferencia'].unique().sum()
    
    count_mark_1 = (submissions_user['mark'] == 1).sum()
    count_mark_0 = (submissions_user['mark'] == 0).sum()
    count_between_0_and_1 = ((submissions_user['mark'] > 0) & (submissions_user['mark'] < 1)).sum()

    sizes = [count_mark_1, count_between_0_and_1, count_mark_0, suma_valores_distintos]
    labels = ['10', 'Other', '0', 'NaN']
    colors = ['#8BC34A', '#FFC107', '#FF4C4C', '#696969']  # Verde, rojo, amarillo, gris oscuro (DimGray)

    # Crear el gráfico circular con fontsize aplicado
    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        textprops={'fontsize': fontsize},
        pctdistance=.7 
    )

    plt.axis('equal')

    
    return plt





def stats_submitions(user_id, aula_id):
    submissions =  pd.read_csv("./../../data/dataset.csv")
    submissions = submissions[['userid', 'aula_id', 'activitat',"activitat_id", 'datesubmitted', 'attempt_number', 'mark', 'count_activities']]


    submissions_user = submissions[submissions["userid"] == user_id]
    submissions_user = submissions_user[ submissions_user["aula_id"] == aula_id]
    submissions_user

    # Número de registros en submissions_user
    num_registros = len(submissions_user)

    # Promedio de la columna 'mark'
    average_mark = submissions_user['mark'].mean()

    # Crear un array con los resultados
    resultado = np.array([num_registros, average_mark])

    # Mostrar el resultado
    return resultado




def submition_temporal_graph(user_id, aula_id):
    fontsize = 18



    submissions =  pd.read_csv("./../../data/dataset.csv")
    submissions = submissions[['userid', 'aula_id', 'activitat',"activitat_id", 'datesubmitted', 'attempt_number', 'mark', 'count_activities']]


    submissions_user = submissions[submissions["userid"] == user_id]
    submissions_user = submissions_user[ submissions_user["aula_id"] == aula_id]

    # Convertir la columna 'datesubmitted' a formato de fecha (sin horas)
    submissions_user['datesubmitted'] = pd.to_datetime(submissions_user['datesubmitted']).dt.date
    # Agrupar por 'datesubmitted' y sumar los valores de 'attempt_number'
    submissions_agrupado = submissions_user.groupby('datesubmitted', as_index=False)['attempt_number'].sum()
    submissions_agrupado



    # Crear el gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(submissions_agrupado['datesubmitted'], submissions_agrupado['attempt_number'], marker='o', linestyle='-', color='#c09268', linewidth=3)
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['left'].set_visible(True)
    plt.gca().spines['bottom'].set_visible(True)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%y'))
    # Personalizar el gráfico para un estilo minimalista
    if(submissions_agrupado.shape[0] != 0):
        plt.xlabel('', fontsize=fontsize)
        plt.ylabel('Submitions', fontsize=fontsize)
        plt.xticks(rotation=45, fontsize = fontsize)
        plt.yticks(np.arange(0, submissions_agrupado['attempt_number'].max() + 1, 5), fontsize= fontsize)
            # Ajustar y mostrar el gráfico
        plt.tight_layout()
    plt.plot
    return plt




def stats_Academic_Record_Mean_Marks(user_id):
    submissions = pd.read_csv("./../../data/dataset.csv")
    submissions = submissions[['userid', 'aula_id', 'activitat', "activitat_id", 'datesubmitted', 'attempt_number', 'mark', 'count_activities']]

    submissions_user = submissions[submissions["userid"] == user_id]
    return submissions_user["mark"].mean()




def stats_Academic_Record_Mean_Final_Grade(user_id):
    submissions = pd.read_csv("./../../data/dataset.csv")
    submissions = submissions[['userid', 'aula_id', 'F_Grade', 'R_Grade']].drop_duplicates()
    submissions


    submissions_user = submissions[submissions["userid"] == user_id]
    # Crea la columna 'Nota_Final' basant-se en la condició donada
    submissions_user['Nota_Final'] = np.where(submissions_user['R_Grade'].notna(), submissions_user['R_Grade'], submissions_user['F_Grade'])

    submissions_user = submissions_user.dropna(subset=['Nota_Final'])

    return submissions_user["Nota_Final"].mean()


def ranking_user(user_id):
    
    submissions =  pd.read_csv("./../../data/dataset.csv")
    submissions_ranking = submissions[["userid", "Nota_Final"]]
    submissions_ranking = submissions_ranking.drop_duplicates()
    submissions_ranking['Nota_Final'] = submissions_ranking['Nota_Final'].str.replace(',', '.')
    submissions_ranking['Nota_Final_Num'] = pd.to_numeric(submissions_ranking['Nota_Final'], errors='coerce')

    submissions_ranking['Media_Nota_Final'] = submissions_ranking.groupby('userid')['Nota_Final_Num'].transform('mean')
    submissions_ranking = submissions_ranking[["userid", "Media_Nota_Final"]]
    submissions_ranking = submissions_ranking.drop_duplicates()

    # Crear un nuevo campo 'Ranking'
    submissions_ranking['Ranking'] = submissions_ranking['Media_Nota_Final'].rank(method='min', ascending=False)

    submissions_ranking = submissions_ranking.drop_duplicates(subset=['userid', 'Media_Nota_Final', 'Ranking'])
    ranking_user = submissions_ranking[submissions_ranking["userid"] == user_id]["Ranking"].values[0]


    return int(ranking_user)



