import dash
import pandas as pd
import plotly.express as px
from dash import dcc
from dash import html
app = dash.Dash(__name__)
df = pd.DataFrame({
   'Fruit': ['Apples', 'Oranges', 'Bananas', 'Apples', 'Oranges', 'Bananas'],
   'Amount': [4, 1, 2, 2, 4, 5],
   'City': ['SF', 'SF', 'SF', 'Montreal', 'Montreal', 'Montreal']
})
fig = px.bar(df, x='Fruit', y='Amount', color='City',
   barmode='group')

app.layout = html.Div(children=[
   html.H1(children='Hello Dash'),
   html.Div(children='''
   Dash: A web application framework for Python.
   '''),
   dcc.Graph(
      id='example-graph',
      figure=fig
   )
])

if __name__ == '__main__':
    # app.run(host='127.0.0.1', port=8080, debug=True, TEMPLATES_AUTO_RELOAD=True)
    app.run_server(debug=False, host='0.0.0.0', port=8050)
