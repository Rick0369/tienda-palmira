import streamlit as st

st.set_page_config(page_title="OLYMPOS - Lina Store", page_icon="👗", layout="centered")

if "stock_body" not in st.session_state:
    st.session_state.stock_body = {"Negro": 5, "Blanco": 4, "Vino": 3, "Azul Noche": 3, "Cafe": 3, "Amarillo": 2}
if "stock_enterizo" not in st.session_state:
    st.session_state.stock_enterizo = {"Negro": 10}

st.title("👗 OLYMPOS - LINA STORE")
st.caption("Inventario en tiempo real | Palmira - 100% desde el celular")
st.divider()

st.subheader("BODY AMARA Ref 3203 - $38.000")
st.write(f"Stock total: {sum(st.session_state.stock_body.values())} unidades | Talla Única")
col1, col2 = st.columns(2)
with col1:
    color_body = st.selectbox("Elige color:", list(st.session_state.stock_body.keys()), key="body_color")
with col2:
    st.metric("Disponibles", st.session_state.stock_body[color_body])

if st.button("🛒 VENDER 1 Body Amara", use_container_width=True):
    if st.session_state.stock_body[color_body] > 0:
        st.session_state.stock_body[color_body] -= 1
        st.success(f"¡Venta registrada! Body Amara {color_body} vendido. Quedan {st.session_state.stock_body[color_body]}")
        st.balloons()
    else:
        st.error("¡Sin stock de ese color!")

st.divider()
st.subheader("Enterizo 070061 - $150.000")
if st.button("🛒 VENDER 1 Enterizo", type="primary", use_container_width=True):
    if st.session_state.stock_enterizo["Negro"] > 0:
        st.session_state.stock_enterizo["Negro"] -= 1
        st.success(f"¡Venta! Quedan {st.session_state.stock_enterizo['Negro']}")
    else:
        st.error("Sin stock")

st.divider()
st.info("💡 Esto es lo que Génesis NO hace desde el celular: control por color en tiempo real.")
