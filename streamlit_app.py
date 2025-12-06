import streamlit as st
from  streamlit_option_menu import option_menu
st.title("Gabriela em uma aventura pelo centro de Assú")
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

if optionMenu == "login":
    st.sucess("Você escolheu realizar o login")
    

if optionMenu == "Cadastro":
    st.sucess("Você escolheu realizar o cadastro")