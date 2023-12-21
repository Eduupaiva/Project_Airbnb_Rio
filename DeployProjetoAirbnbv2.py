import pandas    as pd
import streamlit as st
import xgboost   as xgb
import pickle 

# Definir as variáveis
x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0,
               'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0, 'host_listings_count': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0}

x_listas = {'property_type': ['Apartment', 'Condominium', 'House', 'Outros'],
            'room_type': ['Entire home/apt', 'Hotel room', 'Private room', 'Shared room']}

# Criar um dicionário para armazenar as variáveis categóricas
dicionario = {}

# Adicionar inputs para x_numericos
for item in x_numericos:
    if item == 'latitude' or item == 'longitude':
        valor = st.number_input(f'{item}', step=0.00001, value=0.0, format="%.5f")
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else:
        valor = st.number_input(f'{item}', step=1, value=0)
    x_numericos[item] = valor

# Adicionar inputs para x_tf
for item in x_tf:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    x_tf[item] = 1 if valor == "Sim" else 0

# Adicionar inputs para x_listas
for item in x_listas:
    valor = st.selectbox(f'{item}', x_listas[item])
    for opcao in x_listas[item]:
        chave = f'{item}_{opcao}'
        dicionario[chave] = 1 if opcao == valor else 0


# Atualizar o dicionário com x_numericos e x_tf
dicionario.update(x_numericos)
dicionario.update(x_tf)

# Criar DataFrame com as colunas ordenadas corretamente
colunas_modelo = ['host_is_superhost', 'host_listings_count', 'latitude', 'longitude',
                  'accommodates', 'bathrooms', 'bedrooms', 'beds',
                  'extra_people', 'minimum_nights', 'instant_bookable', 'ano', 'mes',
                  'n_amenities', 'property_type_Apartment', 'property_type_Condominium',
                  'property_type_House', 'property_type_Outros',
                  'room_type_Entire home/apt', 'room_type_Hotel room',
                  'room_type_Private room', 'room_type_Shared room']

# Adicionar zeros para as opções não escolhidas
for coluna in colunas_modelo:
    if coluna not in dicionario:
        dicionario[coluna] = 0

# Criar DataFrame com as colunas ordenadas
valores_x = pd.DataFrame({**dicionario}, columns=colunas_modelo, index=[0])

# Exibir valores no console para depuração
print("Valores originais:")
print(x_numericos)
print(x_tf)
print(dicionario)

# Exibir valores no console após a ordenação
print("\nValores ordenados:")
print(valores_x)

# Botão para prever o valor do imóvel
botao = st.button('Prever Valor do Imovel')

# Prever valor do imóvel ao pressionar o botão
if botao:
    modelo = pickle.load( open( 'model/model_rio.pkl', 'rb' ) )
    preco = modelo.predict(valores_x)
    st.write(preco[0])