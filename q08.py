##
## Agregue el año como una columna a la tabla tbl0.tsv
import pandas as pd
import numpy as np
## llamar archivo
x = pd.read_csv('tbl0.tsv', sep = '\t')
## Agregar el año en una columna al final
x['ano'] = [i.split('-')[0] for i in x['_c3']]
print(x)

