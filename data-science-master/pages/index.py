
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import pandas as pd

column1 = dbc.Col(
    [
        dcc.Markdown(
            """

            ## Music playlist recommender

            This app will recommend music based on given attributes





            """
        ),
    ],
    md=4,
)

df = pd.read_csv(
    'https://raw.githubusercontent.com/Build-Week-Spotify-Song-Suggester-5/Data-Science/master/app/most_popular_spotify_songs.csv')
import plotly.graph_objects as go

categories = ['popularity', 'danceability', 'energy', 'instrumentalness', 'tempo']

fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=[0.75, -0.34, 1.59, -0.39, -0.10],
    theta=categories,
    fill='toself',
    name='New Rules - Dua Lipa'
))
fig.add_trace(go.Scatterpolar(
    r=[0.63, -0.57, 1.38, 0.02, 0.27],
    theta=categories,
    fill='toself',
    name='Apocalypse Dreams - Tame Impala'
))
fig.add_trace(go.Scatterpolar(
    r=[0.52, -0.11, 1.26, -0.39, 0.17],
    theta=categories,
    fill='toself',
    name='On The Line - Jonas Brothers'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[-2, 2]
        )),
    showlegend=False
)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
