import matplotlib.pyplot as plt

import pandas as pd


activities = pd.read_csv("./../../data/activitats.csv", encoding='ISO-8859-1')
marks = pd.read_csv("./../../data/notes.csv", delimiter=';')
submision = pd.read_csv("./../../data/trameses.csv")

pd.options.display.float_format = '{:,.0f}'.format


def clasificar_notas(notas):
    # Lista de resultados
    clasificaciones = []

    # Clasificación de cada nota
    for nota in notas:
        if nota < 5:
            clasificaciones.append("F")
        elif nota < 7:
            clasificaciones.append("P")
        elif nota < 9:
            clasificaciones.append("G")
        else:
            clasificaciones.append("E")
    
    return clasificaciones

def calcular_porcentajes(clasificaciones):
    # Inicializar el conteo de cada categoría
    categorias = ["F", "P", "G", "E"]
    total = len(clasificaciones)
    porcentajes = []

    # Calcular el porcentaje de cada categoría
    for categoria in categorias:
        count = clasificaciones.count(categoria)
        porcentaje = (count / total) 
        porcentajes.append(porcentaje)
    
    return porcentajes

user_id = 155
def pie_chart(user_id):
    
    marks_user = marks[(marks["userid"] == user_id)]
    marks_user
    #887
    #155

    import numpy as np
    marks_user_array = marks_user["F_Grade"].values
    marks_user_array_num = []
    for element in marks_user_array:
        marks_user_array_num.append(float(element.replace(",", ".")))

    marks_user_array_char = clasificar_notas(marks_user_array_num)

    marks_user_array_perc = calcular_porcentajes(marks_user_array_char)

    porcentajes_filtrados = [p for p in marks_user_array_perc if p > 0]
    labels = ['Fail', 'Pass', 'Good', 'Excellent']
    labels_filtradas = [labels[i] for i in range(len(marks_user_array_perc)) if marks_user_array_perc[i] > 0]
    colors = ['skyblue', 'salmon', 'yellowgreen', 'lightcoral'] 
    colors_filtradas = [colors[i] for i in range(len(marks_user_array_perc)) if marks_user_array_perc[i] > 0]

    plt.pie(porcentajes_filtrados, labels=labels_filtradas, colors=colors_filtradas, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 18})

    plt.axis('equal') 

    return plt


