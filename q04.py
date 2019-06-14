##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## Lectura del archivo
import pandas as pd
import numpy as np
x1 = pd.read_csv('tbl1.tsv', sep = '\t')
## Impresion valores unicos
unicos = x1['_c4'].unique()
resultado = []
for x in unicos:
    resultado.append(x.upper())
resultado = sorted(resultado)
print(resultado)
