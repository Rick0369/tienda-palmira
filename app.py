import streamlit as st

st.set_page_config(page_title="Tienda Palmira", page_icon="👕")

st.title("👕 TIENDA DE ROPA - PALMIRA VALLE 👖")
st.subheader("Sistema de Ventas v1.0 - Hecho por Erick")
st.divider()

nombre = st.text_input("👤 Como te llamas")

if nombre:
    st.success(f"¡Hola {nombre}! Bienvenido a la mejor tienda de Palmira 😎 ")

    st.write("### 🔥 PROMOCIONES DE HOY:")
    st.write("_ 👕 Camisas a $30.000")
    st.write("- 👖 Pantalones a $65.000")
    st.write("- 🎁 ¡Lleva 2 pantalones y te regalamos 1 camisa!")

    camisas = st.number_input("👕 cuantas camisas quieres ?", min_value=0 , step=1)
    pantalones = st.number_input("👖Cuantos pantalones quieres?", min_value=0, step=1)

    if st.button("💰 CALCULAR TOTAL"):
        precio_camisa = 30000
        precio_pantalon = 65000
        total = (camisas * precio_camisa) + (pantalones * precio_pantalon)

        st.divider()
        st.write(f"### 🧾 FACTURA PARA: {nombre.upper()}")
        st.write(f"👕 {camisas} camisas x ${precio_camisa} = ${camisas * precio_camisa}")
        st.write(f"👖 {pantalones} pantalones x ${precio_pantalon} = ${pantalones * precio_pantalon}")
        st.write(f"## 💰 TOTAL A PAGAR: ${total} pesos")

        if pantalones >= 2:
            st.balloons()
            st.success(f"🎉 ¡FELICIDADES {nombre}! Te lleva 1 CAMISA GRATIS 🎉")
            st.snow()
        else:
            faltan = 2 - pantalones
            st.warning(f" 💡 Te faltan {faltan} pantalon(es) para ganar una camisa gratis")