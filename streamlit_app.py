import streamlit as st
import requests
from streamlit_lottie import st_lottie 
from streamlit_option_menu import option_menu
import pandas as pd
from google.cloud import firestore

st.image("Imagens/Assuesboço.jpeg", width=400)

st.title("Gabriela em uma aventura pelo centro de Assú")

if "usuario_editando" not in st.session_state:
    st.session_state["usuario_editando"] = None

def carregar_animacao(url: str):
    requisicao = requests.get(url)
    if requisicao.status_code != 200:
        return None
    return requisicao.json()

url_animacao = "https://lottie.host/e84c51e2-924b-4a38-b97e-cb52b6222252/DN8gCtlD93.json"

animacaotempo = carregar_animacao(url_animacao)

dicionario = dict(st.secrets["credencial"])
basedados = firestore.Client.from_service_account_info(dicionario) 

st_lottie(animacaotempo, key="animacaotempo", height=250, width=250)                       
                                  
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

usuarios=basedados.collection("usuarios").stream()

lista_usuarios = []

for usuario in usuarios:
    dados = usuario.to_dict()
    dados["id"] = usuario.id  # opcional: id do documento
    lista_usuarios.append(dados)

if optionMenu == "Login":
    with st.form("formLogin"):
        email = st.text_input("Email:", placeholder="Informe seu email...")
        senha = st.text_input("Senha", placeholder="Informe sua senha...", type="password")
        btnLoginUsuario = st.form_submit_button("Login", use_container_width=True)
    logado = False

    for usuario in lista_usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            logado = True
            usuario_atual= usuario
            st.success("Você escolheu realizar o Login")
           
    if email and senha:
        if not logado:
            st.success("Email ou senha errados...")


if optionMenu == "Cadastro":
    with st.form("formCadastro"):
        nome = st.text_input("Nome:", placeholder="Informe seu nome...")
        apelido = st.text_input("Apelido:", placeholder="Informe seu apelido...")
        idade = st.number_input("Idade:", step=1, min_value=8, max_value=100)
        email = st.text_input("E-mail:", placeholder="Informe seu e-mail...")
        senha = st.text_input("Senha", placeholder="Informe sua senha...", type="password")
        btnCadastroUsuário = st.form_submit_button("Cadastro", use_container_width=True)

        if btnCadastroUsuário:
            if nome and apelido and idade and email and senha:
                novousuario=basedados.collection("usuarios").document(apelido)
                novousuario.set({
                    "nome": nome,
                    "apelido":apelido,
                    "idade": idade,
                    "email": email,
                    "senha": senha
                })
                st.success("Você escolheu realizar o cadastro")
            else:
                st.error("Preencha todos os campos.")

    st.rerun()

df_usuarios = pd.DataFrame(lista_usuarios)

df_usuarios = df_usuarios.drop(columns=["senha"], errors="ignore")
df_usuarios = df_usuarios.drop(columns=["id"], errors="ignore")

st.dataframe(df_usuarios, use_container_width=True)

if logado:
    st.subheader("Editar usuário")
    with st.form(f"form_editar_usuario{usuario_atual['nome']}"):
        nome = st.text_input("Nome", value=usuario_atual.get("nome", ""))
        email = st.text_input("E-mail", value=usuario_atual.get("email", ""))
        apelido = st.text_input("Apelido", value=usuario_atual.get("apelido", ""))
        idade = st.number_input(
            "Idade",
            min_value=8,
            max_value=100,
            step=1,
            value=int(usuario_atual.get("idade", 8))
        )

        btn_salvar = st.form_submit_button("Salvar alterações")

    doc_ref = basedados.collection("usuarios").document(usuario_atual["apelido"])

    if btn_salvar:
        doc_ref.update({
            "nome": nome,
            "apelido": apelido,
            "idade": idade,
            "email": email
        })
        st.session_state["usuario_atualizado"] = True
        st.rerun()

#if st.session_state.get("usuario_atualizado"):
    #st.success("Usuário atualizado com sucesso!")
    #del st.session_state["usuario_atualizado"]
