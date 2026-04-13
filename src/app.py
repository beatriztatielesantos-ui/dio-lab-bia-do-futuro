import streamlit as st
import json

st.set_page_config(page_title="Mentor de Desenvolvimento", layout="centered")

st.title("🤖 Mentor de Desenvolvimento Corporativo")

st.write("Descreva seu objetivo de carreira ou desenvolvimento:")

# carregar perfil
with open("data/perfil_investidor.json") as f:
    perfil = json.load(f)

pergunta = st.text_input("Ex: Quero me tornar líder")

if pergunta:
    st.subheader("📊 Análise do seu perfil")
    st.write(f"Cargo atual: {perfil.get('cargo', 'Não informado')}")
    st.write(f"Objetivo: {perfil.get('objetivo', 'Não informado')}")

    st.subheader("📚 Recomendações")
    st.write("- Comunicação Efetiva")
    st.write("- Fundamentos de Liderança")
    st.write("- Inteligência Emocional")

    st.subheader("📈 Plano de ação")
    st.write("1. Desenvolver habilidades de comunicação")
    st.write("2. Participar de projetos colaborativos")
    st.write("3. Buscar feedback constante")

    st.success("💡 Dica: Comece com pequenos passos e evolua continuamente!")
