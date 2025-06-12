# Parámetros para paredes (como antes)
PARAMETROS_PARED = {
    "comun": {"ladrillos_por_m2": 60, "arena_m3": 0.02, "cemento_kg": 5},
    "hueco": {"ladrillos_por_m2": 30, "arena_m3": 0.015, "cemento_kg": 4},
    "bloque": {"ladrillos_por_m2": 12.5, "arena_m3": 0.01, "cemento_kg": 3}
}

# Nuevos parámetros para contrapisos
PARAMETROS_CONTRAPISO = {
    "cascote": {
        "arena_m3": 0.040,"cemento_kg": 4.5,"cal_kg": 7.8,"cascote_m3": 0.076},
    "piedra": {"arena_m3": 0.080,"cemento_kg": 38,"piedra_m3": 0.080}
}

def calcular_materiales(tipo: str, metros: float, es_contrapiso: bool = False):
    if es_contrapiso:
        datos = PARAMETROS_CONTRAPISO.get(tipo)
        if not datos:
            return {"error": "Tipo de contrapiso no válido. Usar: cascote o piedra"}
        
        return {
            "arena_m3": round(datos["arena_m3"] * metros, 2),
            "cemento_kg": round(datos["cemento_kg"] * metros, 1),
            "cal_kg": round(datos.get("cal_kg", 0) * metros, 1),
            "cascote_m3": round(datos.get("cascote_m3", 0) * metros),
            "piedra_m3": round(datos.get("piedra_m3", 0) * metros)
        }
    else:
        datos = PARAMETROS_PARED.get(tipo)
        if not datos:
            return {"error": "Tipo de pared no válido. Usar: comun, hueco o bloque"}
        
        return {
            "ladrillos": round(datos["ladrillos_por_m2"] * metros),
            "arena_m3": round(datos["arena_m3"] * metros, 2),
            "cemento_kg": round(datos["cemento_kg"] * metros, 1)
        }