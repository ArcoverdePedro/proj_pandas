import pandas as pd
from dash import html, dcc, Dash, Input, Output
import plotly.express as px

pd.set_option('display.max_rows', None)
#pd.set_option('display.max_columns', None)
df = pd.read_csv('Brseriea.csv')



df['mandante_venceu'] = df['gols_mandante'] > df['gols_visitante']
df['visitante_venceu'] = df['gols_visitante'] > df['gols_mandante']


vitorias_mandante_time = df.groupby(['time_mandante'])['mandante_venceu'].sum()
#vitorias_visitante_time = df.groupby('time_visitante')['visitante_venceu'].sum()
#print('Vitórias por mandante:', vitorias_mandante_time)
#print('Vitórias por visitante:', vitorias_visitante_time)

print (vitorias_mandante_time)
#print (df.info())