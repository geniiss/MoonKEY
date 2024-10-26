def Academic_Record(user_id):
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
    marks_user = marks[(marks["userid"] == user_id)]

    #Transforma los formatos de fecha UNIX
    marks_user.loc[:,'P_Grade_Date'] = pd.to_datetime(marks_user.loc[:,'P_Grade_Date'], unit='s').dt.date
    marks_user.loc[:,'F_Grade_Date'] = pd.to_datetime(marks_user.loc[:,'F_Grade_Date'], unit='s').dt.date
    marks_user.loc[:,'R_Grade_Date'] = pd.to_datetime(marks_user.loc[:,'R_Grade_Date'], unit='s').dt.date

    return marks_user[marks["aula_id"] == aula_id]


def pie_chart_submissions_user(user_id):
    submissions =  pd.read_csv("./../../data/dataset.csv")
    submissions = submissions[['userid', 'aula_id', 'activitat',"activitat_id", 'datesubmitted', 'attempt_number', 'mark', 'count_activities']]
    submissions

    submissions_user = submissions[submissions["userid"] == user_id]
    submissions_user

    conteo_por_aula = submissions_user.groupby('aula_id').size()

    # Convertir el conteo a un DataFrame y renombrar la columna
    conteo_por_aula = conteo_por_aula.rename('conteo_registros').reset_index()

    # Unir el conteo como una nueva columna en el DataFrame original
    submissions_user = submissions_user.merge(conteo_por_aula, on='aula_id', how='left')
    submissions_user['diferencia'] = submissions_user['count_activities'] - submissions_user['conteo_registros']



    # Paso 2: Contar registros por aula_id y agregarlo como columna 'conteo_registros'
    # Agrupamos el DataFrame submissions_user por 'aula_id' y contamos el número de registros en cada grupo
    conteo_por_aula = submissions_user.groupby('aula_id').size()

    # Renombramos la serie a 'conteo_registros' y la convertimos en un DataFrame
    conteo_por_aula = conteo_por_aula.rename('conteo_registros').reset_index()

    # Eliminar la columna 'conteo_registros' si ya existe en submissions_user
    if 'conteo_registros' in submissions_user.columns:
        submissions_user = submissions_user.drop(columns=['conteo_registros'])

    # Realizamos un merge con submissions_user para agregar el conteo de registros como una nueva columna
    submissions_user = submissions_user.merge(conteo_por_aula, on='aula_id', how='left')

    # Paso 3: Crear la columna 'diferencia' como la resta entre 'count_activities' y 'conteo_registros'
    # Restamos la columna 'conteo_registros' de 'count_activities' y guardamos el resultado en una nueva columna 'diferencia'
    submissions_user['diferencia'] = submissions_user['count_activities'] - submissions_user['conteo_registros']

    # Paso 4: Calcular suma_valores_distintos, la suma de los valores únicos en 'diferencia'
    # Obtenemos los valores únicos en la columna 'diferencia' y calculamos su suma
    suma_valores_distintos = submissions_user['diferencia'].unique().sum()
    




    count_mark_1 = (submissions_user['mark'] == 1).sum()

    # Contar el número de registros donde mark es igual a 0
    count_mark_0 = (submissions_user['mark'] == 0).sum()

    # Contar el número de registros donde mark está entre 0 y 1
    count_between_0_and_1 = ((submissions_user['mark'] > 0) & (submissions_user['mark'] < 1)).sum()


    sizes = [count_mark_1, count_between_0_and_1, count_mark_0, suma_valores_distintos]
    labels = ['10', 'Other', '0',  'NaN']
    colors = ['#8BC34A', '#FFC107', '#FF4C4C', '#696969']  # Verde, rojo, amarillo, gris oscuro (DimGray)

    # Crear el gráfico circular
    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors
    )

    # Asegurarse de que el gráfico sea circular
    plt.axis('equal')

    # # Añadir la leyenda
    # plt.legend(labels, loc="best", title="Categorías")

    # Mostrar el gráfico
    plt.show()

def pie_chart_submissions_user_aula(user_id, aula_id):
    submissions =  pd.read_csv("./../../data/dataset.csv")
    submissions = submissions[['userid', 'aula_id', 'activitat',"activitat_id", 'datesubmitted', 'attempt_number', 'mark', 'count_activities']]


    submissions_user = submissions[submissions["userid"] == user_id]
    submissions_user = submissions_user[ submissions_user["aula_id"] == aula_id]
    submissions_user

    conteo_por_aula = submissions_user.groupby('aula_id').size()

    # Convertir el conteo a un DataFrame y renombrar la columna
    conteo_por_aula = conteo_por_aula.rename('conteo_registros').reset_index()

    # Unir el conteo como una nueva columna en el DataFrame original
    submissions_user = submissions_user.merge(conteo_por_aula, on='aula_id', how='left')
    submissions_user['diferencia'] = submissions_user['count_activities'] - submissions_user['conteo_registros']



    # Paso 2: Contar registros por aula_id y agregarlo como columna 'conteo_registros'
    # Agrupamos el DataFrame submissions_user por 'aula_id' y contamos el número de registros en cada grupo
    conteo_por_aula = submissions_user.groupby('aula_id').size()

    # Renombramos la serie a 'conteo_registros' y la convertimos en un DataFrame
    conteo_por_aula = conteo_por_aula.rename('conteo_registros').reset_index()

    # Eliminar la columna 'conteo_registros' si ya existe en submissions_user
    if 'conteo_registros' in submissions_user.columns:
        submissions_user = submissions_user.drop(columns=['conteo_registros'])

    # Realizamos un merge con submissions_user para agregar el conteo de registros como una nueva columna
    submissions_user = submissions_user.merge(conteo_por_aula, on='aula_id', how='left')

    # Paso 3: Crear la columna 'diferencia' como la resta entre 'count_activities' y 'conteo_registros'
    # Restamos la columna 'conteo_registros' de 'count_activities' y guardamos el resultado en una nueva columna 'diferencia'
    submissions_user['diferencia'] = submissions_user['count_activities'] - submissions_user['conteo_registros']

    # Paso 4: Calcular suma_valores_distintos, la suma de los valores únicos en 'diferencia'
    # Obtenemos los valores únicos en la columna 'diferencia' y calculamos su suma
    suma_valores_distintos = submissions_user['diferencia'].unique().sum()
    




    count_mark_1 = (submissions_user['mark'] == 1).sum()

    # Contar el número de registros donde mark es igual a 0
    count_mark_0 = (submissions_user['mark'] == 0).sum()

    # Contar el número de registros donde mark está entre 0 y 1
    count_between_0_and_1 = ((submissions_user['mark'] > 0) & (submissions_user['mark'] < 1)).sum()
    

    sizes = [count_mark_1, count_between_0_and_1, count_mark_0, suma_valores_distintos]
    labels = ['10', 'Other', '0',  'NaN']
    colors = ['#8BC34A', '#FFC107', '#FF4C4C', '#696969']  # Verde, rojo, amarillo, gris oscuro (DimGray)

    # Crear el gráfico circular
    plt.pie(
        sizes,
        labels=labels,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors
    )

    # Asegurarse de que el gráfico sea circular
    plt.axis('equal')

    # # Añadir la leyenda
    # plt.legend(labels, loc="best", title="Categorías")

    # Mostrar el gráfico
    plt.show()