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
    
    if op == "Metros a Pies": 
        st.success(f"{val} metros son {val * 3.28084:.4f} pies.")
    elif op == "Pies a Metros": 
        st.success(f"{val} pies son {val / 3.28084:.4f} metros.")
    elif op == "Centímetros a Pulgadas": 
        st.success(f"{val} cm son {val / 2.54:.4f} pulgadas.")
    elif op == "Pulgadas a Centímetros": 
        st.success(f"{val} pulgadas son {val * 2.54:.4f} cm.")
    elif op == "Kilómetros a Millas": 
        st.success(f"{val} km son {val / 1.60934:.4f} millas.")
    elif op == "Millas a Kilómetros": 
        st.success(f"{val} millas son {val * 1.60934:.4f} km.")
    elif op == "Yardas a Metros": 
        st.success(f"{val} yardas son {val * 0.9144:.4f} metros.")
    elif op == "Metros a Yardas": 
        st.success(f"{val} metros son {val / 0.9144:.4f} yardas.")

# --- 2. MASA Y VOLUMEN ---
elif tanda == "Masa y Volumen":
    st.header("⚖️ Masa y Líquidos")
    op = st.selectbox("Conversión:", [
        "Gramos a Onzas", "Onzas a Gramos", "Litros a Galones", "Galones a Litros",
        "Litros a Mililitros", "Mililitros a Litros", "Gramos a Kilogramos",
        "Kilogramos a Gramos", "Kilogramos a Libras", "Libras a Kilogramos"
    ])
    val = st.number_input("Ingresá el valor:", value=0.0)
    
    if op == "Gramos a Onzas": 
        st.success(f"{val} g = {val / 28.3495:.4f} oz")
    elif op == "Onzas a Gramos":
        st.success(f"{val} oz = {val * 28.3495:.4f} g")
    elif op == "Kilogramos a Libras": 
        st.success(f"{val} kg = {val * 2.20462:.4f} lb")
    elif op == "Libras a Kilogramos":
        st.success(f"{val} lb = {val / 2.20462:.4f} kg")
    elif op == "Litros a Galones":
        st.success(f"{val} L = {val / 3.78541:.4f} gal")
    elif op == "Galones a Litros":
        st.success(f"{val} gal = {val * 3.78541:.4f} L")

# --- 3. TIEMPO Y FECHAS ---
elif tanda == "Tiempo y Fechas":
    st.header("⏳ Tiempo")
    op = st.selectbox("Conversión:", [
        "Segundos a Minutos", "Minutos a Segundos", "Horas a Minutos", "Minutos a Horas",
        "Días a Horas", "Horas a Días", "Semanas a Días", "Años a Días"
    ])
    val = st.number_input("Valor de tiempo:", value=0.0)
    
    if op == "Segundos a Minutos": 
        st.info(f"{val} seg = {val / 60:.2f} min")
    elif op == "Minutos a Segundos":
        st.info(f"{val} min = {val * 60:.0f} seg")
    elif op == "Horas a Minutos":
        st.info(f"{val} h = {val * 60:.0f} min")
    elif op == "Años a Días": 
        st.info(f"{val} años ≈ {val * 365:.0f} días")

# --- 4. FÍSICA Y MECÁNICA ---
elif tanda == "Física y Mecánica":
    st.header("⚡ Física")
    op = st.selectbox("Cálculo:", [
        "Velocidad (Distancia y Tiempo)", "Fuerza (Masa y Aceleración)", 
        "Presión (Fuerza y Área)", "Densidad (Masa y Volumen)"
    ])
    
    if op == "Velocidad (Distancia y Tiempo)":
        d = st.number_input("Distancia (m):")
        t = st.number_input("Tiempo (s):", min_value=0.0001)
        st.success(f"Velocidad: {d/t:.2f} m/s")
    elif op == "Fuerza (Masa y Aceleración)":
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
    
    if op == "Área Círculo":
        r = st.number_input("Radio:")
        st.success(f"Área: {math.pi * r**2:.4f}")
    elif op == "Volumen Esfera":
        r = st.number_input("Radio:")
        st.success(f"Volumen: {(4/3) * math.pi * r**3:.4f}")
    elif op == "Área Rectángulo":
        b = st.number_input("Base:")
        h = st.number_input("Altura:")
        st.success(f"Área: {b * h:.2f}")

# --- 6. SALUD Y TEMPERATURA ---
elif tanda == "Salud y Temperatura":
    st.header("🌡️ Salud y Temperatura")
    op = st.selectbox("Opción:", [
        "Celsius a Fahrenheit", "Fahrenheit a Celsius", "IMC", 
        "Kelvin a Celsius", "Celsius a Kelvin"
    ])
    
    if op == "Celsius a Fahrenheit":
        c = st.number_input("Ingresá °C:", value=0.0)
        st.success(f"{c} °C son {(c * 9/5) + 32:.2f} °F")
        
    elif op == "Fahrenheit a Celsius":
        f = st.number_input("Ingresá °F:", value=32.0)
        st.success(f"{f} °F son {(f - 32) * 5/9:.2f} °C")

    elif op == "IMC":
        st.subheader("📊 Calculadora de Índice de Masa Corporal")
        peso = st.number_input("Peso (kg):", value=70.0, step=0.1)
        altura = st.number_input("Altura (m):", value=1.70, step=0.01)
        
        if altura > 0:
            imc = peso / (altura ** 2)
            st.info(f"Tu IMC es: **{imc:.2f}**")
            
            # Clasificación del IMC
            if imc < 18.5:
                st.warning("Clasificación: **Bajo peso**")
            elif 18.5 <= imc < 25:
                st.success("Clasificación: **Peso normal (Saludable)**")
            elif 25 <= imc < 30:
                st.warning("Clasificación: **Sobrepeso**")
            else:
                st.error("Clasificación: **Obesidad**")
        else:
            st.error("La altura debe ser mayor a 0.")

    elif op == "Celsius a Kelvin":
        c = st.number_input("Ingresá °C:", value=0.0)
        st.success(f"{c} °C son {c + 273.15:.2f} K")
        
    elif op == "Kelvin a Celsius":
        k = st.number_input("Ingresá K:", value=273.15)
        st.success(f"{k} K son {k - 273.15:.2f} °C")
