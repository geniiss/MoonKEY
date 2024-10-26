import pandas as pd

activities = pd.read_csv("C:/Users/anhin/Documents/GitHub/MoonKEY/data/activitats.csv", encoding='ISO-8859-1')
marks = pd.read_csv("C:/Users/anhin/Documents/GitHub/MoonKEY/data/notes.csv", delimiter=';')
submision = pd.read_csv("C:/Users/anhin/Documents/GitHub/MoonKEY/data/trameses.csv")

print(marks)
#print(marks)
#print(activities)
#print(submision)

pd.options.display.float_format = '{:,.0f}'.format
user_31 = submision[(submision["userid"] == 31) & (submision["activitat_id"] == 362)]
print(user_31.shape)

print(user_31)


