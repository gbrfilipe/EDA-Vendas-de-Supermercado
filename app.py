import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from funcoes import tratar_dataset
from funcoes import importar_foto_perfil
from funcoes import descrever_dados

# Variáveis de execução
headers = ["ID", "filial", "cidade", "tipo_cliente", "genero", "linha_de_produto", "preco_unitario", "quantidade", "taxa_5%",
           "total", "data", "hora", "forma_pagamento", "custo_produtos", "porcentagem_margem_bruta", "renda_bruta", "avaliacao"]

df = tratar_dataset('supermarket_sales.csv', headers)
df['semana'] = pd.DatetimeIndex(df['data']).week
df['apenas_horas'] = df['hora'].str[:2]


foto_enzo = importar_foto_perfil('fotos/enzo.jpg')
foto_elizabeth = importar_foto_perfil('fotos/elizabeth.jpg')
foto_elton = importar_foto_perfil('fotos/elton.jpg')
foto_gabriel = importar_foto_perfil('fotos/gabriel.jpg')
foto_anonima = "https://v5j9q4b5.rocketcdn.me/wp-content/uploads/2019/04/7-curiosidades-intrigantes-e-imperdiveis-sobre-os-anonymous.jpg"

# Sidebar
with st.sidebar:
    st.multiselect('Selecione um filtro:',
                   df.columns[1:6])
    visibilidade_colunas = st.checkbox(label='Exibir colunas')

width = st.sidebar.slider("plot width", 1, 25, 16)
height = st.sidebar.slider("plot height", 1, 25, 6)


# Cabeçalho do projeto
st.markdown('''
            # Análise de vendas de supermercado
            Uma análise exploratória dos dados de vendas de uma rede de supermercados para conclusão do modulo Técnicas de Programação 2 do curso de Python e Dados - ADA
            ''')


exibir_fotos = st.checkbox('Exibir fotos dos desenvolvedores?')
if exibir_fotos:
    foto_enzo = importar_foto_perfil('fotos/enzo.jpg')
    foto_elizabeth = importar_foto_perfil('fotos/elizabeth.jpg')
    foto_elton = importar_foto_perfil('fotos/elton.jpg')
    foto_gabriel = importar_foto_perfil('fotos/gabriel.jpg')
else:
    foto_enzo = foto_anonima
    foto_elizabeth = foto_anonima
    foto_elton = foto_anonima
    foto_gabriel = foto_anonima

# Fotos do perfil
st.image([foto_enzo, foto_elizabeth, foto_elton, foto_gabriel],
         caption=['Enzo', 'Elizabeth', 'Elton', 'Gabriel'], width=100)


# Introdução
st.markdown('''
            # Introdução
            
            Sabemos que o mercado de varejo carece de informações mais acertivas e análise mais aprofundadas de suas vendas.
            
            Nesse sentido, buscamos realizar uma analise dos dados de vendas de uma rede de supermercados a fim de encontrar padrões de compra, nichos de produtos entre os consumidores membros da rede e os não membros.
            
            O objetivo deste projeto é trasnformar os dados de três supermercados e informações úteis para ter uma rápida análise dos seguintes fatores:
            ''')

# Descrição do projeto colapsada (expander)
with st.expander('**Descrição da base de dados**', expanded=True):
    st.dataframe(descrever_dados(df))
    if visibilidade_colunas:
        st.write('**Colunas do dataset:**')
        st.dataframe(df.columns)


# Análises Univariadas
st.markdown('''
            # Análises Univariadas
            ''')

fig, ax = plt.subplots(figsize=(width, height))
sns.countplot(data=df, x='tipo_cliente', hue='genero')
st.pyplot(fig)

with st.expander('Explicação do gráfico acima:', expanded=False):
    st.write("""De acordo com a análise acima, observamos que os clientes membros são de maioria do gênero feminino, já nos clientes normais (não membros), são de maioria de gênero masculino.""")

fig, ax = plt.subplots(figsize=(width, height))
sns.histplot(data=df, x='custo_produtos', kde=True)
st.pyplot(fig)

with st.expander('Explicação do gráfico acima:', expanded=False):
    st.write("""De acordo com a análise acima, observamos produtos com menor custo, há o maior numero de vendas.""")


# Análises Bivariadas
st.markdown('''
            # Análises Bivariadas
            ''')


fig, ax = plt.subplots(figsize=(width, height))
sns.barplot(data=df,
            x="linha_de_produto",
            y="quantidade",
            estimator="sum",
            errorbar=None)
st.pyplot(fig)

with st.expander('Explicação do gráfico acima:', expanded=False):
    st.write("""De acordo com a análise acima, observamos as categorias de itens vendidos, onde a categoria 'electronic accessories', é a categoria de maior venda.""")

fig = plt.figure(figsize=(width, height))
df.groupby('forma_pagamento')['total'].sum().plot(kind="pie", autopct='%.1f%%')
st.pyplot(fig)

with st.expander('Explicação do gráfico acima:', expanded=False):
    st.write("""De acordo com a análise acima, observamos a porcentagem da forma de pagamento das compras.""")

st.dataframe(df.groupby('cidade')['avaliacao'].mean())
with st.expander('Explicação da tabela acima:', expanded=False):
    st.write("""De acordo com a tabela acima, fizemos a média entre os valores de avaliação dos clientes por cidade, e com isso, concluímos que a loja da cidade de Naypyitaw tem a melhor avaliação média.""")


# Análises Multivariadas
st.markdown('''
            # Análises Multivariadas
            ''')

fig, ax = plt.subplots(figsize=(width, height))
sns.barplot(data=df,
            x="cidade",
            y="total",
            estimator="mean",
            hue="linha_de_produto",
            errorbar=None)
st.pyplot(fig)

with st.expander('Explicação do gráfico acima:', expanded=False):
    st.write("""De acordo com a análise acima, observamos a comparação de diferentes categorias por cidade, onde nem sempre uma categoria é a maior em todas as cidades.""")

fig, ax = plt.subplots(figsize=(width, height))
sns.lineplot(data=df, x='semana', y='total', hue='genero', estimator='sum')
st.pyplot(fig)

with st.expander('Explicação do gráfico acima:', expanded=False):
    st.write(
        """De acordo com a análise acima, observamos a variação do total das vendas por semana divididos por gênero, onde na semana 8, houve uma queda nas compras de ambos os gêneros.""")

df_sorted = df.sort_values(by='apenas_horas')


fig, ax = plt.subplots(figsize=(width, height))
sns.histplot(data=df_sorted, x='apenas_horas', kde=True)
st.pyplot(fig)

with st.expander('Explicação do gráfico acima:', expanded=False):
    st.write(
        """De acordo com a análise acima, observamos a distribuição do numero de vendas pelo horário, onde aproximadamente as 20 horas, temos uma queda das vendas.""")
