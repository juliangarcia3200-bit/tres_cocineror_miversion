# Ejercicio 1- Función para calcular la depreciación por método de línea recta.

def calcular_depreciacion_linea_recta(costo_activo, valor_salvamento, vida_util):

    if vida_util <= 0:
        raise ValueError("La vida útil debe ser mayor que cero.")
    depreciacion_anual = (costo_activo - valor_salvamento) / vida_util

    return depreciacion_anual

# Calcular base de depreciación (costo - valor de salvamento)
    base_depreciable = costo_activo - valor_salvamento

# Calcular depreciación anual
    depreciacion_anual = base_depreciable / vida_util

    return depreciacion_anual

costo_del_activo = 50000000
valor_residual = 5000000
años_de_vida_util = 5

try:
    depreciacion = calcular_depreciacion_linea_recta(costo_del_activo, valor_residual, años_de_vida_util)
    print(f"La depreciación anual es: {depreciacion}")  
except ValueError as e:
    print(e)            


# Ejercicio 4-  COGS y margen bruto (método básico). 

def calcular_cogs_y_margen_bruto(inventario_inicial, compras_netas, inventario_final, ingresos_por_ventas):
    
    # 1. Calcular el Costo de los Bienes Vendidos (COGS)
    cogs = inventario_inicial + compras_netas - inventario_final

    # 2. Calcular el Margen Bruto
    margen_bruto = ingresos_por_ventas - cogs

    # 3. Devolver ambos resultados
    return cogs, margen_bruto

ingresos_ventas = 250000000
inventario_inicial = 50000000
compras = 150000000
inventario_final = 70000000

cogs_calculado, margen_bruto_calculado = calcular_cogs_y_margen_bruto(
    inventario_inicial,
    compras,
    inventario_final,
    ingresos_ventas
)
print(f"El Costo de los Bienes Vendidos (COGS) es: {cogs_calculado}")
print(f"El Margen Bruto es: {margen_bruto_calculado}")  


       