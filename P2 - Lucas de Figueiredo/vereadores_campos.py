# importar bibliotecas
import streamlit as st
import pandas as pd

#Adendo, não foi utilizado columns para renomear as colunas pois apresentava problema na hora de exibir os dados

DATA_URL = "candidatos_vereador_campos.csv"

@st.cache
def load_data():
    #Dados dos candidatos a vereadores de Campos extraídos do csv com base na coluna Partido
    data = pd.read_csv(DATA_URL, index_col='NM_PARTIDO')

    print(data)

    return data

#Carregando os Dados do data frame e os labels para multiselects
df = load_data()
labels = df.DS_SIT_TOT_TURNO.unique().tolist()
labels_genero = df.DS_GENERO.unique().tolist()
labels_instrucao = df.DS_GRAU_INSTRUCAO.unique().tolist()
labels_raca = df.DS_COR_RACA.unique().tolist()

#SIDEBAR
#Parâmetros e número de ocorrências
st.sidebar.header("Selecione os Parâmetros dos candidatos que deseja visualizar:")
info_sidebar = st.sidebar.empty()

#Input Partido
partido_filter = int(st.sidebar.text_input('Escolha o Partido desejado pelo número:', value='22', max_chars=2, placeholder='22'))

#Multiselect da Situação
select_situacao = st.sidebar.multiselect(
    label="Escolha a situação do candidato",
    options=labels,
    default=['ELEITO POR MÉDIA', 'SUPLENTE', '#NULO#', 'NÃO ELEITO', 'ELEITO POR QP']
)

#Slider da Idade
idade_filter = st.sidebar.slider('A idade do Candidato:',  18, 80, (18, 80))
a = idade_filter[0]
b = idade_filter[1]

#Multiselect do Genero
select_genero = st.sidebar.multiselect(
    label="Escolha o gênero dos candidatos",
    options=labels_genero,
    default=['MASCULINO', 'FEMININO']
)

#Multiselect da Escolaridade
select_instrucao = st.sidebar.multiselect(
    label="Escolha a escolaridade dos candidatos",
    options=labels_instrucao,
    default=['ENSINO MÉDIO COMPLETO', 'ENSINO FUNDAMENTAL COMPLETO', 'ENSINO FUNDAMENTAL INCOMPLETO', 'SUPERIOR INCOMPLETO', 'SUPERIOR COMPLETO', 'LÊ E ESCREVE']
)

#Multiselect Etnia
select_raca = st.sidebar.multiselect(
    label="Escolha a etnia dos candidatos",
    options=labels_raca,
    default=['PARDA', 'BRANCA', 'PRETA', 'INDÍGENA', 'AMARELA', 'NÃO INFORMADO']
)

#Legenda abaixo dos filtros
st.sidebar.markdown(""" A base de dados de candidatos a vereadores no município de Campos dos Goytacazes foi extraída a partir de tratamento
no google colab.""")

filtered_df = df[(df.DS_COR_RACA.isin(select_raca))&
                 (df.DS_GRAU_INSTRUCAO.isin(select_instrucao))&
                 (df.DS_GENERO.isin(select_genero))&
                 (df.DS_SIT_TOT_TURNO.isin(select_situacao))&
                 (df.NR_PARTIDO == partido_filter)&
                 (df.NR_IDADE_DATA_POSSE.between(a, b))]

#MAIN
st.title("Candidatos a Eleição de Campos dos Goytacazes por Filtros e Partidos")
st.markdown('Exibindo candidatos de acordo com os filtros aplicados.')

#Exibe o Dataframe, ele é atualizado conforme os filtros são selecionados
st.write(filtered_df)

#Preciso de 5,4 pontos na p2 somando com os outros trabalhos ;)