import streamlit as st
st.title("E-Book")
st.write("Para a formação do livro foi realizada a análise de documentos históricos" \
" da cidade e análise bibliográfica de artigos, também o uso do chatGPT e Canva para a formação" \
" estética do material e criação da personagem. ")
st.write("É importante ressaltar que a escolha da Gabriela como uma menina negra não foi feita ao accaso," \
" e sim para que mostrasse a representação afrobrasileira do município, e para trazer a tona sujeitos invisibilizados" \
" no processo de construção do repasse de histórias e acontecimentos.")
"---"
st.write("Acesso ao e-book")
st.write("Acesso ao artigo")
"---"
st.write("Por favor, responda ao formulário para ajudar a manter a atualização e andamento do projeto!")

nasceu = st.text_input("Você nasceu em assú?", placeholder="Responda com sim ou não...")
mora = st.text_input("Você reside em assú atualmente?", placeholder="Responda com sim ou não...")
trabalho = st.text_input("Você reside em outra cidade porém estuda/trabalha em assú?", placeholder="Responda com sim ou não...")
conhecer = st.text_input("Você conhece a história do centro de assú?", placeholder="Responda com sim ou não...")
escola = st.text_input("Você teve contato com a história do centro durante o seu período escolar", placeholder="Responda com sim ou não...")
plataforma = st.text_input("Você acha que o site ajudou ou motivou você a conhecer mais sobre a parte histórica da cidade?", placeholder="Responda com sim ou não...")
sugestoes = st.text_input("Sugestões:", placeholder="Escreva sugestões para o melhoramento da plataforma...")