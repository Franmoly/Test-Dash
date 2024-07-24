#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
#from jupyter_dash import JupyterDash


# Configurar la aplicación Dash
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

# Datos de ejemplo
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

# Crear la figura
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# Definir el layout de la aplicación
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Div(children='''Dash: A web application framework for Python.'''),
    dcc.Graph(id='example-graph', figure=fig)
])


# Ejecutar el servidor en modo "external"
if __name__ == '__main__':
    app.run_server(debug=True)





