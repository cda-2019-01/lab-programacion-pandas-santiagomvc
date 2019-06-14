##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c4
## de la tabla tbl1.tsv
import pandas as pd
import numpy as np
## leer archivo
x1 = pd.read_csv('tbl1.tsv', sep = '\t')
## Construccion de tabla
x1temp = x1.groupby('_c0')['_c4'].apply(list)
x1b = pd.DataFrame()
x1b['_c0'] = x1temp.keys()
x1b['lista'] = [elem for elem in x1temp]
x1b['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in x1b['lista']]
print(x1b)
