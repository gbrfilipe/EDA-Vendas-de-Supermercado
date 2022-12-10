import streamlit as st
from funcoes import tratar_dataset
from funcoes import importar_foto_perfil
from funcoes import descrever_dados

headers = ["ID", "filial", "cidade", "tipo_cliente", "genero", "linha_de_produto", "preco_unitario", "quantidade", "taxa_5%", "total", "data", "hora", "forma_pagamento", "custo_produtos", "porcentagem_margem_bruta", "renda_bruta", "avaliacao"]

df = tratar_dataset('supermarket_sales.csv', headers)

foto_enzo = importar_foto_perfil('fotos/enzo.jpg')
foto_elizabeth = importar_foto_perfil('fotos/elizabeth.jpg')
foto_elton = importar_foto_perfil('fotos/elton.jpg')
foto_gabriel = importar_foto_perfil('fotos/gabriel.jpg')

# # Cabeçalho do projeto
#             ![Enzo](https://avatars.githubusercontent.com/u/90116258?v=4)
#             ![Elizabeth](https://avatars.githubusercontent.com/u/76952671?v=4)
#             ![Elizabeth](https://avatars.githubusercontent.com/u/52720089?v=4)
#             ![Gabriel](https://avatars.githubusercontent.com/u/48440319?v=4)

st.markdown('''
            # Análise de vendas de supermercado
            Uma análise exploratória dos dados de vendas de uma rede de supermercados para conclusão do modulo Técnicas de Programação 2 do curso de Python e Dados - ADA
            ''')

# Fotos do perfil
st.image([foto_enzo, foto_elizabeth, foto_elton, foto_gabriel], caption=['Enzo','Elizabeth', 'Elton', 'Gabriel'], width=100)


# Introdução
st.markdown('''
            # Introdução
            
            Sabemos que o mercado de varejo carece de informações mais acertivas e análise mais aprofundadas de suas vendas.
            
            Nesse sentido, buscamos realizar uma analise dos dados de vendas de uma rede de supermercados a fim de encontrar padrões de compra, nichos de produtos entre os consumidores membros da rede e os não membros.
            
            O objetivo deste projeto é trasnformar os dados de três supermercados e informações úteis para ter uma rápida análise dos seguintes fatores:
            ''')

with st.expander('**Descrição da base de dados**'):
    st.dataframe(descrever_dados(df))