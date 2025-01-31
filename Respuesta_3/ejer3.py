#EJERCICIO 3:
#Costo de vida en paises de america.

import pandas as pd
datos=pd.read_csv('living.csv')

costo_vida_paises_america = datos[datos['Continent'] == 'America']
costo_vida_paises_america[['Countries', 'Cost of living, 2017']].to_csv('Costo_de_vida_en_Paises_de_America.csv', index=False)
print(costo_vida_paises_america[['Countries', 'Cost of living, 2017']])
