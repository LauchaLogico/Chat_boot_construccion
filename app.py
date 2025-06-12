import streamlit as st
from calculadora import calcular_materiales

# Configuración
st.title("🏗️ Chatbot Constructor Avanzado")
st.write("**Di 'Hola' para empezar**")

# Historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Lógica del chat
if prompt := st.chat_input("Escribe tu mensaje..."):
    # Agregar mensaje de usuario
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generar respuesta
    prompt_lower = prompt.lower()
    response = ""
    
    if "hola" in prompt_lower:
        response = "¡Hola! ¿Qué necesitas calcular?\n1. Pared (ladrillos)\n2. Contrapiso"
    
    elif "pared" in prompt_lower or any(t in prompt_lower for t in ["comun", "hueco", "bloque"]):
        tipo = next((t for t in ["comun", "hueco", "bloque"] if t in prompt_lower), None)
        if tipo:
            try:
                metros = float(next(s for s in prompt.split() if s.replace("m2", "").replace(",", ".").replace(".", "", 1).isdigit()))
                materiales = calcular_materiales(tipo, metros, es_contrapiso=False)
                response = f"""
                🧱 **Materiales para {metros}m² de pared ({tipo})**:
                - Ladrillos: {materiales['ladrillos']} unidades
                - Arena: {materiales['arena_m3']} m³
                - Cemento: {materiales['cemento_kg']} kg
                """
            except:
                response = "❌ Especifica los metros cuadrados. Ej: '5m2 de ladrillo comun'"
        else:
            response = "Indica el tipo de ladrillo: comun, hueco o bloque"
    
    elif "contrapiso" in prompt_lower or any(t in prompt_lower for t in ["cascote", "piedra"]):
        tipo = next((t for t in ["cascote", "piedra"] if t in prompt_lower), None)
        if tipo:
            try:
                metros = float(next(s for s in prompt.split() if s.replace("m2", "").replace(",", ".").replace(".", "", 1).isdigit()))
                materiales = calcular_materiales(tipo, metros, es_contrapiso=True)
                response = f"""
                🏗️ **Materiales para {metros}m² de contrapiso ({tipo})**:
                - Arena: {materiales['arena_m3']} m³
                - Cemento: {materiales['cemento_kg']} kg
                - {'Cascote' if tipo == 'cascote' else 'Piedra'}: {materiales.get('cascote_m3', materiales.get('piedra_m3', 0))} m³
                {f"- Cal: {materiales['cal_kg']} kg" if tipo == "cascote" else ""}
                """
            except:
                response = "❌ Especifica los metros cuadrados. Ej: '10m2 de contrapiso cascote'"
        else:
            response = "Indica el tipo de contrapiso: cascote o piedra"
    
    else:
        response = "No entendí. Ejemplos:\n- '5m2 de ladrillo hueco'\n- '10m2 de contrapiso piedra'"

    # Mostrar respuesta
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})