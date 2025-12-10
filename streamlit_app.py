import streamlit as st
import requests
#from streamlit_lottie import as st_lottie 
from  streamlit_option_menu import option_menu
st.title("Gabriela em uma aventura pelo centro de Assú")

#def carregar_animacao(url: str):
    #requisicao = requests.get(url)
    #if requisicao.status_code != 200:
        #return None
    #if requisicao.json()

#url_animacao = ""

#animacaotempo = carregar_animacao(url_animacao
                                  
#st_lottie(animacaotempo, key="animacaotempo")                         
                                  
st.write(
    "A cidade de assú sobretudo o seu centro histórico e cultural é demasiadamente desprestigiado" \
    " mesmo trazendo uma carga histórico-cultural riquíssima, com figuras como a baronesa, os baobás," \
    " casarões, terras ricas em lavoura e agropecuária entre diversos outros pontos. Dessa forma, o projeto" \
    " apresentado nesse site tem o objetivo de apontar a relevância da história do município assuense e a importância" \
    " de você cidadão ter conhecimento acerca da trajetória histórica da comunidade, com foco no público infantojuvenil."
)
"---"
st.write(
    "Esse site lhe dara acesso a um livro digital infantojuvenil contando a história do centro historico de Assú e conhecer " \
    "um pouco mais sobre o projeto. Para isso crie uma conta abaixo ou entre se ja tiver uma."
)

optionMenu = option_menu(
    menu_title="...",
    options=["Login","Cadastro"],
    icons=["house", "envelope"],
    default_index=0,
    orientation="horizontal",
)

if optionMenu == "Login":
    with st.form("formLogin"):
        usuario = st.text_input("Usuário:", placeholder="Informe seu usuário...")
        senha = st.text_input("Senha", placeholder="Informe sua senha...", type="password")
        btnLoginUsuario = st.form_submit_button("Login", use_container_width=True)
    st.success("Você escolheu realizar o Login")
    

if optionMenu == "Cadastro":
    with st.form("formCadastro"):
        nome = st.text_input("Nome:", placeholder="Informe seu nome...")
        usuario = st.text_input("Usuário:", placeholder="Informe seu usuário...")
        idade = st.number_input("Idade:", step=1, min_value=8, max_value=100)
        email = st.text_input("E-mail:", placeholder="Informe seu e-mail...")
        senha = st.text_input("Senha", placeholder="Informe sua senha...", type="password")
        btnCadastroUsuário = st.form_submit_button("Cadastro", use_container_width=True)
    st.success("Você escolheu realizar o cadastro")