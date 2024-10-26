import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def model_87_P_dataset(dataset, aula_id):
    dataset['attempt_number'] = dataset['attempt_number'].fillna(10)
    dataset['attempt_number'] = dataset['attempt_number'].astype("float")
    dataset['mark'] = dataset['mark'].fillna(0)
    dataset['average_attempt_number'] = dataset.groupby(['userid', 'aula_id'])['attempt_number'].transform('mean')
    dataset['average_mark'] = dataset.groupby(['userid', 'aula_id'])['mark'].transform('mean')
    dataset = dataset[["userid", "aula_id", "average_attempt_number", "average_mark", "NOT_Presented_P", "P_Grade", "P_Grade_Date", "NOT_Presented_F", "F_Grade", "F_Grade_Date", "NOT_Presented_R", "R_Grade", "R_Grade_Date", "rank_P", "rank_F", "rank_R"]]
    dataset = dataset.drop_duplicates()
    dataset = dataset[dataset["aula_id"] == aula_id]
    dataset = dataset[dataset["NOT_Presented_P"] == 0]
    dataset = dataset[dataset["NOT_Presented_F"] == 0]
    
    return dataset

def model_87_P_function(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model_87_P = LinearRegression()
    model_87_P.fit(X_train, y_train)
    y_pred = model_87_P.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    info = {"Mean Square Error": mse,
            "R^2": r2,
            "Cofficients": model_87_P.coef_,
            "Intercept": model_87_P.intercept_}

    return {"model": model_87_P, "info": info}

def prediction_model(path_model, X_target):
    model = joblib.load(path_model)
    prediccion = model.predict(X_target)
    return prediccion[0]

dataset = pd.read_csv('./../../data/dataset.csv')
dataset_model_87_P = model_87_P_dataset(dataset, 141)
model_87_P = model_87_P_function(dataset_model_87_P[["P_Grade", "average_attempt_number"]], dataset_model_87_P["F_Grade"])

user_789_aula_141 = dataset[(dataset["userid"] == 789) & (dataset["aula_id"] == 141)][["P_Grade", "average_attempt_number"]].drop_duplicates()
print(user_789_aula_141)

print(prediction_model('./../../data/models/model_87_P.pkl', user_789_aula_141))
print(dataset[(dataset["userid"] == 789) & (dataset["aula_id"] == 141)][["F_Grade"]].drop_duplicates())
#joblib.dump(model_87_P["model"], './../../data/models/model_87_P.pkl')

'''
OBRIR MODEL

with open('modelo_entrenado.pkl', 'rb') as archivo:
    modelo_cargado = pickle.load(archivo)

# Usar el modelo cargado para hacer predicciones
prediction = modelo_cargado.predict([[5]])
print(prediccion)
'''