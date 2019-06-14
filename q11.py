##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
import pandas as pd
import numpy as np
## Leer archivo
x2 = pd.read_csv('tbl2.tsv', sep = '\t')
## Construccion de tabla
x2['_c5'] = x2['_c5a'] + ":" + x2['_c5b'].astype('str')
x2temp = x2.groupby('_c0')['_c5'].apply(list)
x2b = pd.DataFrame()
x2b['_c0'] = x2temp.keys()
x2b['lista'] = [elem for elem in x2temp]
x2b['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in x2b['lista']]
print(x2b)

