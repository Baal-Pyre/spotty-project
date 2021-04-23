# # Imports from 3rd party libraries
# import dash
# import dash_bootstrap_components as dbc
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import plotly.express as px
#
# # Imports from this application
# from app import app
#
# # 2 column layout. 1st column width = 4/12
# # https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
# column1 = dbc.Col(
#     [
#         dcc.Markdown(
#             """
#
#             ## Your Value Proposition
#
#             Emphasize how the app will benefit users. Don't emphasize the underlying technology.
#
#             ✅ RUN is a running app that adapts to your fitness levels and designs personalized workouts to help you improve your running.
#
#             ❌ RUN is the only intelligent running app that uses sophisticated deep neural net machine learning to make your run smarter because we believe in ML driven workouts.
#
#             """
#         ),
#         dcc.Link(dbc.Button('Your Call To Action', color='primary'), href='/predictions')
#     ],
#     md=4,
# )
#
# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)
#
# column2 = dbc.Col(
#     [
#         dcc.Graph(figure=fig),
#     ]
# )
#
# layout = dbc.Row([column1, column2])


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