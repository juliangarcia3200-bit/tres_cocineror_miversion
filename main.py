# 2. Función para calcular el estado de resultados simplificado

def er_simplificado():
    ingresos = float(input(f"Valor de Los Ingresos: "))
    costos = float(input(f"Valor de Los Costos de Ventas: "))
    gastos = float(input(f"Valor de Los Gastos: "))
    u_bruta = ingresos - costos
    u_ant_imp = u_bruta - gastos
    m_bruto = u_bruta / ingresos
    m_ant_imp = u_ant_imp / ingresos
    impuesto = 0.35 * u_ant_imp if u_ant_imp > 0 else 0
    u_neta = u_ant_imp - impuesto
    m_neto = u_neta / ingresos
    return print(f"""Estado de Resultados simplificado 2024
                 
      Ingresos:                {ingresos:,.2f}
      costos:                  {costos:,.2f}
      Utilidad Bruta:          {u_bruta:,.2f}
      Margen Bruto:            {m_bruto:.2%}
      
      Gastos:                  {gastos:,.2f}
      Utilidad Ant. Impuestos: {u_ant_imp:,.2f}
      Margen Ant. Impuestos:   {m_ant_imp:.2%}
      
      Impuesto de Renta:       {impuesto:,.2f}
      
      Utilidad Neta:           {u_neta:,.2f}
      Margen Neto:             {m_neto:.2%}
                 """)

er_simplificado()