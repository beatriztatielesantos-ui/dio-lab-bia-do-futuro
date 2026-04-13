# 🤖 Agente Inteligente de Educação Corporativa com IA Generativa

## 📌 Contexto

Os assistentes virtuais em educação corporativa estão evoluindo de sistemas reativos para agentes inteligentes e proativos, capazes de orientar o desenvolvimento profissional de forma personalizada.

Este projeto propõe a criação de um agente que:

- Antecipa necessidades de desenvolvimento dos colaboradores  
- Personaliza trilhas de aprendizagem  
- Apoia planos de desenvolvimento (PDI)  
- Garante respostas confiáveis e alinhadas à estratégia da empresa  

---

## 🎯 Objetivo

Desenvolver um agente de IA que atue como mentor de desenvolvimento profissional, apoiando colaboradores na evolução de carreira dentro da organização.

---

## 🧠 Funcionalidades do Agente

- 📊 Análise do perfil do colaborador  
- 🎯 Identificação de gaps de desenvolvimento  
- 📚 Recomendação de cursos e trilhas  
- 🧭 Criação de planos de desenvolvimento (PDI)  
- 💡 Sugestões práticas de evolução profissional  

---

## 🏗️ Arquitetura da Solução

O agente utiliza uma abordagem baseada em contexto (RAG):

1. Entrada do colaborador (chat)
2. Consulta à base de dados (perfil, cursos, trilhas)
3. Análise do objetivo profissional
4. Geração de recomendações personalizadas
5. Validação de consistência
6. Resposta ao usuário

---

## 🔒 Segurança e Confiabilidade

- Respostas baseadas apenas em dados internos  
- Não inventa cursos ou trilhas  
- Mantém alinhamento com políticas da empresa  
- Evita recomendações genéricas ou incoerentes  

---

## 📁 Estrutura do Repositório

lab-agente-educacao/
│
├── README.md
├── data/
├── docs/
├── src/
├── assets/
└── examples/

---

## 📊 Base de Conhecimento

O agente utiliza dados mockados para simular um ambiente corporativo:

| Arquivo | Descrição |
|--------|----------|
| perfil_colaborador.json | Perfil e objetivos do colaborador |
| historico_aprendizado.csv | Cursos realizados |
| trilhas.json | Trilhas disponíveis |
| cursos.json | Catálogo de cursos |

---

## 💬 Prompts do Agente

O comportamento do agente é definido por prompts que garantem:

- Comunicação clara e consultiva  
- Recomendações personalizadas  
- Respostas seguras e confiáveis  

---

## 💻 Aplicação

Protótipo desenvolvido com:

- Python  
- Streamlit  
- Integração com LLM (API ou modelo local)  

---

## 📈 Avaliação e Métricas

O agente será avaliado com base em:

- Precisão das recomendações  
- Aderência ao perfil do colaborador  
- Clareza das respostas  
- Segurança (sem alucinações)  

---

## 🎤 Pitch

O projeto inclui um pitch apresentando:

- Problema  
- Solução  
- Diferenciais  
- Impacto organizacional  

---

## 🚀 Como Executar

pip install -r requirements.txt  
streamlit run src/app.py  

---

## 💡 Diferencial do Projeto

Este agente atua como um mentor de carreira corporativo, indo além de um chatbot tradicional:

- Analisa contexto do colaborador  
- Sugere caminhos personalizados  
- Apoia decisões de desenvolvimento  

---

## 📌 Considerações Finais

Este projeto demonstra como a IA pode transformar o desenvolvimento corporativo, tornando-o mais estratégico, personalizado e orientado a resultados.
