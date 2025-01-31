#EJERCICIO 2:
#Paises costo de vida bajo

import pandas as pd
datos=pd.read_csv('living.csv')


#Aplicar orden ascendente:
top_10_paises_costo_vida_bajo=datos.sort_values('Cost of living, 2017', ascending=True).head(10)
top_10_paises_costo_vida_bajo[['Countries','Cost of living, 2017']].to_csv('top 10 paises con costo de vida bajo.csv', index=False)
print(f"{top_10_paises_costo_vida_bajo[['Countries','Cost of living, 2017']]}")
