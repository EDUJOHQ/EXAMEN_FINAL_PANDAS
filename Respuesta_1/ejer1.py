#EJERCICIO 1:
#Paises con costo de vida alto:

import pandas as pd
datos=pd.read_csv('living.csv')


top_10_paises_costo_vida_alto=datos[['Countries','Cost of living, 2017']].head(10)
print(f"10 paises con costo de vida alto son: {top_10_paises_costo_vida_alto[['Countries','Cost of living, 2017']]}")

top_10_paises_costo_vida_alto[['Countries', 'Cost of living, 2017']].to_csv('top 10 paises con costo de vida alto.csv', index=False)
