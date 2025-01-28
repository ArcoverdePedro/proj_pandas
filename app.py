import pandas as pd
#from dash import html, dcc, Dash, Input, Output
#import plotly.express as px

pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df = pd.read_csv('Brseriea.csv')


def maisvenceumandante(data):
    data['mandante_venceu'] = data['gols_mandante'] > data['gols_visitante']
    data['visitante_venceu'] = data['gols_visitante'] > data['gols_mandante']
    vitorias_mandante_time = data.groupby(['time_mandante'])['mandante_venceu'].sum()
    print(vitorias_mandante_time)

def maisvenceuvistante(data):
    data['mandante_venceu'] = data['gols_mandante'] > data['gols_visitante']
    data['visitante_venceu'] = data['gols_visitante'] > data['gols_mandante']
    vitorias_visitante_time = data.groupby(['time_visitante'])['visitante_venceu'].sum()
    print(vitorias_visitante_time)

def maispontosmandante(data):
    data['mandante_venceu'] = data['gols_mandante'] > data['gols_visitante']
    data['visitante_venceu'] = data['gols_visitante'] > data['gols_mandante']
    mandante_venceu = data.groupby(['time_mandante'])['mandante_venceu'].sum() * 3
    data['mandante_empate'] = data['gols_mandante'] == data['gols_visitante']
    mandante_empate = data.groupby(['time_mandante'])['mandante_empate'].sum()
    pontos_mandante_time = mandante_venceu + mandante_empate
    print(mandante_venceu)


#maisvenceumandante(df)
#maisvenceuvistante(df)
#maispontosmandante(df)

