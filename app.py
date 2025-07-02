import streamlit as st
import tempfile
from backend import get_haircut_advice

st.set_page_config(page_title="Conseiller Coupe de Cheveux", layout="centered")

st.title("💇‍♂️ Conseiller de coupe de cheveux par IA")
st.write("Uploade une image de ton visage pour obtenir une suggestion de coupe de cheveux adaptée.")

uploaded_file = st.file_uploader("Choisir une image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Image chargée", use_container_width=True)

    if st.button("Proposer une coupe"):
        with st.spinner("Analyse en cours..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name

            advice = get_haircut_advice(tmp_path)
            st.subheader("💡 Coupe suggérée :")
            st.write(advice)
