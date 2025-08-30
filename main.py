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

#3. funcion para Amortización de un Credito
def calculo_amortización():
    n = int(input("Ingrese el número de pagos (n): "))
    i = float(input("Ingrese la tasa de interés periódica (i) en decimal: "))
    P = float(input("Ingrese el monto del préstamo (P): "))
    
    #Calculo de la cuota fija del credito
    if i == 0:
        cuota = P / n
    else:
        cuota = (P * i) / (1 - (1 + i) ** -n)
        
    print(f"La amortización periódica es: {cuota:.2f}")
    
    #Tabla de amortización
    print("\nTabla de Amortización:")
    print(f"{'Periodo':<10}{'Pago':<15}{'Interés':<15}{'Principal':<15}{'Saldo':<15}")
    saldo = P
    for periodo in range(1, n + 1):
        interes = saldo * i
        principal = cuota - interes
        saldo -= principal
        print(f"{periodo:<10}{cuota:<15.2f}{interes:<15.2f}{principal:<15.2f}{saldo:<15.2f}")               
    return cuota

amortizacion = calculo_amortización()


#6. Punto de Equilibrio (Unidades y Ventas)
def punto_equilibrio():
    costos_fijos = float(input("Ingrese los costos fijos totales: "))
    precio_venta = float(input("Ingrese el precio de venta por unidad: "))
    costo_variable = float(input("Ingrese el costo variable por unidad: "))
    
    if precio_venta <= costo_variable:
        print("El precio de venta debe ser mayor que el costo variable para calcular el punto de equilibrio.")
        return None, None
    
    #Calculo del Punto de Equilibrio en Unidades
    punto_equilibrio_unidades = costos_fijos / (precio_venta - costo_variable)
    
    #Calculo del Punto de Equilibrio en Ventas
    punto_equilibrio_ventas = punto_equilibrio_unidades * precio_venta
    
    print(f"Punto de Equilibrio en Unidades: {punto_equilibrio_unidades:.2f} unidades")
    print(f"Punto de Equilibrio en Ventas: ${punto_equilibrio_ventas:.2f}")
    
    return punto_equilibrio_unidades, punto_equilibrio_ventas   

unidades, ventas = punto_equilibrio()
