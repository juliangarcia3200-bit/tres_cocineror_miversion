from datetime import date #Importa la clase "date" para trabajar con fechas(año, mes, día)
from typing import List, Dict, Any, Tuple #Importa tipos para "type hints" (listas, diccionarios, etc)

#Definimos la funcion principal
def conciliacion_bancaria(mov_libro: List[Dict[str, Any]], #Movimientos del libro contable
                          mov_banco: List[Dict[str, Any]], #Movimientos del banco
                          tolerancia_dias: int = 3 #Dias de diferencia permitidos
) -> Dict[str, List[Dict[str, Any]]]: #Devuelve un diccionario con tres listas de movimientos.
    """
    Empareja movimientos del libro contable con los del banco, considerando una tolerancia en días.
    Retorna movimientos conciliados, no conciliados del libro y no conciliados del banco.
    """
    usados_banco = set() #Conjunto para rastrear movimientos del banco ya emparejados
    coincdentes = [] #Lista para movimientos conciliados
    solo_libro = [] #Lista para movimientos solo en el libro

    #Recorremos cada movimiento del libro contable
    for i, ml in enumerate(mov_libro):
        match_idx = None #Indice del movimiento del banco que coincide
        #Recorremos cada movimiento del banco
        for j, mb in enumerate(mov_banco):
            if j in usados_banco:
                continue #Si ya fue usado, saltamos
            mismo_monto = abs(ml['monto'] - mb['monto']) < 1e-6 #Compara si los montos son iguales (con tolerancia de 0.000001)
            dias = abs((ml['fecha'] - mb['fecha']).days) #Calcula la diferencia en días entre las fechas
            if mismo_monto and dias <= tolerancia_dias:
                match_idx = j #Si coinciden, guardamos el indice
                break
        if match_idx is not None:
            usados_banco.add(match_idx) #Marcamos el movimiento del banco como usado
            coincdentes.append({'libro': ml, 'banco': mov_banco[match_idx]}) #Agregamos a la lista de conciliados
        else:
            solo_libro.append(ml) #Si no hay coincidencia, agregamos a la lista de solo libro
    solo_banco = [mb for j, mb in enumerate(mov_banco) if j not in usados_banco] #Movimientos del banco no usados
    return {
        'coincidentes': coincdentes, #Movimientos conciliados
        'solo_libro': solo_libro, #Movimientos solo en el libro
        'solo_banco': solo_banco #Movimientos solo en el banco
    }
