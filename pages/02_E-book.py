import streamlit as st
from google.cloud import firestore

st.title("E-Book")

dicionario = dict(st.secrets["credencial"])
basedados2 = firestore.Client.from_service_account_info(dicionario) 

colunas = st.columns(2)
colunas[0].image("Imagens/1.png", width=250)
colunas[1].image("Imagens/9.png", width=250)

st.write("Para a formação do livro foi realizada a análise de documentos históricos" \
" da cidade e análise bibliográfica de artigos, também o uso do chatGPT e Canva para a formação" \
" estética do material e criação da personagem. ")
st.write("É importante ressaltar que a escolha da Gabriela como uma menina negra não foi feita ao accaso," \
" e sim para que mostrasse a representação afrobrasileira do município, e para trazer a tona sujeitos invisibilizados" \
" no processo de construção do repasse de histórias e acontecimentos.")
"---"

st.markdown("Abaixo você podera ter acesso ao artigo explicando todo o projeto e o ebook do livro apenas clicando no botão indicado.")

with open("Imagens/ebook.pdf", "rb") as pdf:
    st.download_button(
        label="📄 Baixar ebook",
        data=pdf,
        file_name="ebook.pdf",
        mime="application/pdf"
    )

with open("Imagens/Artigo.pdf", "rb") as pdf:
    st.download_button(
        label="📄 Baixar Artigo",
        data=pdf,
        file_name="Artigo.pdf",
        mime="application/pdf"
    )
"---"
st.write("Por favor, responda ao formulário para ajudar a manter a atualização e andamento do projeto!")

with st.form("formFormulario"):
    nasceu=st.selectbox("Você nasceu em assú?",["","Sim", "Não"] )
    mora=st.selectbox("Você reside em assú atualmente?",["","Sim", "Não"])
    trabalho =st.selectbox("Você reside em outra cidade porém estuda/trabalha em assú?", ["","Sim", "Não"])
    conhecer =st.selectbox("Você conhece a história do centro de assú?", ["","Sim", "Não"])
    escola =st.selectbox("Você teve contato com a história do centro durante o seu período escolar", ["","Sim", "Não"])
    plataforma =st.selectbox("Você acha que o site ajudou ou motivou você a conhecer mais sobre a parte histórica da cidade?", ["","Sim", "Não"])
    sugestoes = st.text_input("Sugestões:", placeholder="Escreva sugestões para o melhoramento da plataforma...")
    btnformFormulario = st.form_submit_button("Salvar respostas")

    if btnformFormulario:
            if nasceu and mora and trabalho and conhecer and escola and plataforma and sugestoes:
                novoquestionario=basedados2.collection("usuarios").document(apelido)
                novoquestionario.set({
                    "Você nasceu em assú?": nasceu,
                    "Você reside em assú atualmente?": mora,
                    "Você reside em outra cidade porém estuda/trabalha em assú?": trabalho,
                    "Você conhece a história do centro de assú?": conhecer,
                    "Você teve contato com a história do centro durante o seu período escolar": escola,
                    "Você acha que o site ajudou ou motivou você a conhecer mais sobre a parte histórica da cidade?": plataforma,
                    "Sugestões:": sugestoes
                })
                st.success("Suas respostas foram salvas com sucesso!")
            else:
                st.error("Preencha todos os campos.")

    st.rerun()
    