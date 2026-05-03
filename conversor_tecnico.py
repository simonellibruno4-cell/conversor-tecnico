import streamlit as st
import math

# Configuración de la página
st.set_page_config(page_title="Conversor Técnico ", page_icon="⚙️")

st.title("⚙️ Conversor de Unidades Técnico")

# --- BARRA LATERAL: SELECCIÓN DE TANDA ---
tanda = st.sidebar.radio("Seleccioná una Categoría:", 
    ["Distancia y Longitud", "Masa y Volumen", "Tiempo y Fechas", "Física y Mecánica", "Geometría", "Salud y Temperatura"])

# --- 1. DISTANCIA Y LONGITUD ---
if tanda == "Distancia y Longitud":
    st.header("📏 Longitud y Distancia")
    op = st.selectbox("Conversión:", [
        "Metros a Pies", "Pies a Metros", "Centímetros a Pulgadas", "Pulgadas a Centímetros",
        "Kilómetros a Millas", "Millas a Kilómetros", "Yardas a Metros", "Metros a Yardas",
        "Millas a Pies", "Pies a Millas"
    ])
    val = st.number_input("Ingresá el valor:", value=0.0)
    
    if "." in op: st.success(f"{val} metros son {val * 3.28084:.4f} pies.")
    elif "." in op: st.success(f"{val} pies son {val / 3.28084:.4f} metros.")
    elif "." in op: st.success(f"{val} cm son {val / 2.54:.4f} pulgadas.")
    elif "." in op: st.success(f"{val} pulgadas son {val * 2.54:.4f} cm.")
    elif "." in op: st.success(f"{val} km son {val / 1.60934:.4f} millas.")
    elif "." in op: st.success(f"{val} millas son {val * 1.60934:.4f} km.")
    elif "." in op: st.success(f"{val} yardas son {val * 0.9144:.4f} metros.")
    elif "." in op: st.success(f"{val} metros son {val / 0.9144:.4f} yardas.")

# --- 2. MASA Y VOLUMEN ---
elif tanda == "Masa y Volumen":
    st.header("⚖️ Masa y Líquidos")
    op = st.selectbox("Conversión:", [
        "Gramos a Onzas", "Onzas a Gramos", "Litros a Galones", "Galones a Litros",
        "Litros a Mililitros", "Mililitros a Litros", "Gramos a Kilogramos",
        "Kilogramos a Gramos", "Kilogramos a Libras", "Libras a Kilogramos"
    ])
    val = st.number_input("Ingresá el valor:", value=0.0)
    
    if "." in op: st.success(f"{val} g = {val / 28.3495:.4f} oz")
    elif "." in op: st.success(f"{val} kg = {val * 2.20462:.4f} lb")
    # Agregá los demás de tu lista aquí siguiendo el mismo patrón

# --- 3. TIEMPO Y FECHAS ---
elif tanda == "Tiempo y Fechas":
    st.header("⏳ Tiempo")
    op = st.selectbox("Conversión:", [
        "Segundos a Minutos", "Minutos a Segundos", "Horas a Minutos", "Minutos a Horas",
        "Días a Horas", "Horas a Días", "Segundos a Horas", "Horas a Segundos",
        "Días a Segundos", "Segundos a Días", "Semanas a Días", "Años a Días"
    ])
    val = st.number_input("Valor de tiempo:", value=0.0)
    
    if "." in op: st.info(f"{val} seg = {val / 60:.2f} min")
    elif "." in op: st.info(f"{val} años = {val * 365:.0f} días")

# --- 4. FÍSICA Y MECÁNICA ---
elif tanda == "Física y Mecánica":
    st.header("⚡ Física")
    op = st.selectbox("Cálculo:", [
        "Velocidad (Distancia y Tiempo)", "Fuerza (Masa y Aceleración)", 
        "Energía", "Potencia", "Presión", "Densidad",
        "Frecuencia", "Periodo"
    ])
    
    if "." in op:
        d = st.number_input("Distancia:")
        t = st.number_input("Tiempo:", min_value=0.0001)
        st.success(f"Velocidad: {d/t:.2f} unidades/t")
    elif "." in op:
        m = st.number_input("Masa (kg):")
        a = st.number_input("Aceleración (m/s²):")
        st.success(f"Fuerza: {m * a:.2f} N")

# --- 5. GEOMETRÍA ---
elif tanda == "Geometría":
    st.header("📐 Geometría")
    op = st.selectbox("Figura:", [
        "Área Círculo", "Volumen Cilindro", "Área Triángulo", 
        "Volumen Esfera", "Área Rectángulo", "Volumen Cubo"
    ])
    
    if "Área Círculo" in op:
        r = st.number_input("Radio:")
        st.success(f"Área: {math.pi * r**2:.4f}")
    elif "Volumen Esfera" in op:
        r = st.number_input("Radio:")
        st.success(f"Volumen: {(4/3) * math.pi * r**3:.4f}")

# --- 6. SALUD Y TEMPERATURA ---
elif tanda == "Salud y Temperatura":
    st.header("🌡️ Salud y Temperatura")
    op = st.selectbox("Opción:", [
        "Celsius a Fahrenheit", "Fahrenheit a Celsius", "IMC", 
        "Kelvin a Celsius", "Celsius a Kelvin"
    ])
    
    if "Celsius a Fahrenheit" in op:
        c = st.number_input("°C:")
        st.success(f"{(c * 9/5) + 32:.2f} °F")
    elif "IMC" in op:
        p = st.number_input("Peso (kg):")
        h = st.number_input("Altura (m):")
        if h > 0: st.info(f"Tu IMC es {p / (h**2):.2f}")