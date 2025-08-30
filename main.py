import pandas as pd
from datetime import datetime
from conciliacion_bancaria import conciliacion_bancaria

df_libro = pd.read_csv('libro.csv')
df_libro['fecha'] = pd.to_datetime(df_libro['fecha']).dt.date
mov_libro = df_libro.to_dict("records")

df_banco = pd.read_csv('banco.csv')
df_banco['fecha'] = pd.to_datetime(df_banco['fecha']).dt.date
mov_banco = df_banco.to_dict("records")

resultado = conciliacion_bancaria(mov_libro, mov_banco, tolerancia_dias=3)
print("Movimientos conciliados:")
for item in resultado['coincidentes']:
    print(f"Libro: {item['libro']} <=> Banco: {item['banco']}") 