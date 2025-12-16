import streamlit as st
import requests
from streamlit_lottie import st_lottie 
st.title("Junte-se a nós!")
st.subheader("Entenda como ajudar ou fazer parte do projeto")

def carregar_animacao(url: str):
    requisicao = requests.get(url)
    if requisicao.status_code != 200:
        return None
    return requisicao.json()

url_animacao = "https://lottie.host/17583529-1f62-4860-b0d2-3a179146a03a/aDUzs7phXd.json"
animacaoajuda = carregar_animacao(url_animacao)
st_lottie(animacaoajuda, key="animacaotempo", height=300, width=300)

"---"
st.write("Se você possui interesse em participar ativamente do projeto como desing/corretor de texto, entre outros" \
" serviços que podem ser ofertados por favor entre em contato conosco através do email: projetogabriela@gmail.com")
st.write("Se você quer ajudar financeiramente para que possamos publicar o livro, pois somos duas estuantes sem" \
" uma renda extra para isso, pode colocar sua contribuição na chave pix: xxxxxxx")

