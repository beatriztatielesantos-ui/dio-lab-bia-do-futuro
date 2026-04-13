import streamlit as st
import json
import pandas as pd
import streamlit as st
import json
import pandas as pd
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


objetivo = pergunta.lower()

st.subheader("📊 Análise do perfil")
st.write(f"Cargo: {perfil.get('cargo')}")
st.write(f"Objetivo: {perfil.get('objetivo')}")

# identificar categorias
categorias = []

if any(p in objetivo for p in ["lider", "gestor", "equipe"]):
    categorias.append("liderança")

if any(p in objetivo for p in ["comunicação", "falar", "apresentar"]):
    categorias.append("comunicação")

if any(p in objetivo for p in ["carreira", "crescer", "promoção"]):
    categorias.append("carreira")

if not categorias:
    categorias = perfil.get("interesses", [])

# histórico
st.subheader("📅 Histórico de desenvolvimento")
st.dataframe(historico)

cursos_feitos = historico["acao"].tolist()

# recomendações inteligentes
recomendacoes = [
    curso["nome"]
    for curso in cursos
    if curso["categoria"] in categorias
    and curso["nome"] not in cursos_feitos
]

st.subheader("📚 Recomendações personalizadas")

for curso in recomendacoes:
    st.write(f"- {curso}")

st.subheader("📈 Plano de desenvolvimento")

st.write("1. Iniciar cursos recomendados")
st.write("2. Aplicar no dia a dia")
st.write("3. Buscar feedback")
st.write("4. Revisar evolução mensal")

st.success("💡 Evolução contínua gera crescimento profissional!")
