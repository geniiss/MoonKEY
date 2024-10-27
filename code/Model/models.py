import pandas as pd
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def model_F_dataset(dataset, aula_id):
    if aula_id == 141:
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
    else:
        print("This model hasn't been developed yet")
        return None
    
def model_F_function(X, y, aula_id):
    if aula_id == 141:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        model_F = LinearRegression()
        model_F.fit(X_train, y_train)
        y_pred = model_F.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        info = {"Mean Square Error": mse,
                "R^2": r2,
                "Cofficients": model_F.coef_,
                "Intercept": model_F.intercept_}

        return {"model": model_F, "info": info}
    else:
        print("This model hasn't been developed yet")
        return None

def model_R_dataset(dataset, aula_id):
    if aula_id == 141:
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
        dataset = dataset[dataset["NOT_Presented_R"] == 0]
        return dataset
    else:
        print("This model hasn't been developed yet")
        return None
        
def model_R_function(X, y, aula_id):
    if aula_id == 141:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        model_R = LinearRegression()
        model_R.fit(X_train, y_train)
        y_pred = model_R.predict(X_test)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        info = {"Mean Square Error": mse,
                "R^2": r2,
                "Cofficients": model_R.coef_,
                "Intercept": model_R.intercept_}

        return {"model": model_R, "info": info}
    else:
        print("This model hasn't been developed yet")
        return None

def prediction_model(path_model_F, path_model_R, user_id, aula_id):
    dataset = pd.read_csv('./../../data/dataset.csv')
    dataset_model_141_F = model_F_dataset(dataset, 141)
    dataset = pd.read_csv('./../../data/dataset.csv')
    dataset_model_141_R = model_R_dataset(dataset, 141)
    user_789_aula_141_F = dataset_model_141_F[(dataset_model_141_F["userid"] == user_id) & (dataset_model_141_F["aula_id"] == aula_id)][["P_Grade", "average_attempt_number"]].drop_duplicates()
    user_789_aula_141_R = dataset_model_141_R[(dataset_model_141_R["userid"] == user_id) & (dataset_model_141_R["aula_id"] == aula_id)][["P_Grade", "F_Grade", "average_attempt_number"]].drop_duplicates()
    model_F = joblib.load(path_model_F)
    model_R = joblib.load(path_model_R)
    prediction_F = model_F.predict(user_789_aula_141_F)
    prediction_R = model_R.predict(user_789_aula_141_R)

    return prediction_F[0], prediction_R[0]


'''dataset = pd.read_csv('./../../data/dataset.csv')
dataset_model_141_F = model_F_dataset(dataset, 141)
model_141_F = model_F_function(dataset_model_141_F[["P_Grade", "average_attempt_number"]], dataset_model_141_F["F_Grade"], 141)

dataset = pd.read_csv('./../../data/dataset.csv')
dataset_model_141_R = model_R_dataset(dataset, 141)
model_141_R = model_R_function(dataset_model_141_R[["P_Grade", "F_Grade", "average_attempt_number"]], dataset_model_141_R["R_Grade"], 141)

user_789_aula_141_F = dataset_model_141_F[(dataset_model_141_F["userid"] == 789) & (dataset_model_141_F["aula_id"] == 141)][["P_Grade", "average_attempt_number"]].drop_duplicates()
user_789_aula_141_R = dataset_model_141_R[(dataset_model_141_R["userid"] == 789) & (dataset_model_141_R["aula_id"] == 141)][["P_Grade", "F_Grade", "average_attempt_number"]].drop_duplicates()



print(prediction_model('./../../data/models/model_141_P.pkl', user_789_aula_141_F))
print(dataset[(dataset["userid"] == 789) & (dataset["aula_id"] == 141)][["F_Grade"]].drop_duplicates())

print(prediction_model('./../../data/models/model_141_R.pkl', user_789_aula_141_R))
print(dataset[(dataset["userid"] == 789) & (dataset["aula_id"] == 141)][["R_Grade"]].drop_duplicates())'''

'''

joblib.dump(model_141_F["model"], './../../data/models/model_141_P.pkl')
joblib.dump(model_141_R["model"], './../../data/models/model_141_R.pkl')


OBRIR MODEL

with open('modelo_entrenado.pkl', 'rb') as archivo:
    modelo_cargado = pickle.load(archivo)

# Usar el modelo cargado para hacer predicciones
prediction = modelo_cargado.predict([[5]])
print(prediccion)
'''