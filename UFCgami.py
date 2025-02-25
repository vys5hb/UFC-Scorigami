import sqlite3
import pandas as pd
import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
import os

# Connect SQL database to Python
conn = sqlite3.connect('ufc_scorigami.db')
cursor = conn.cursor()
df = pd.read_sql_query("SELECT * FROM ufc_fights;", conn)

# Find all unique fight ending times
unique_scorigami = df[['round', 'time']].drop_duplicates().reset_index(drop=True)

# Convert time to seconds for easier manipulation
def time_to_seconds(time_str):
    minutes, seconds = map(int, time_str.split(':'))
    return minutes * 60 + seconds
unique_scorigami['total_seconds'] = unique_scorigami['time'].apply(time_to_seconds)

# Map (round, total_seconds) to True
time_occurrences = {(row['round'], row['total_seconds']): True for _, row in unique_scorigami.iterrows()}

# Create time labels from 0:00 to 5:00
time_labels = [f"{i//60}:{i%60:02d}" for i in range(301)]

# Create the DataFrame structure
heatmap_df = pd.DataFrame(index=range(1, 6), columns=time_labels)

# Fill in the DataFrame with "✅" for True and "" for False
for round_num in range(1, 6):
    for sec in range(301):
        if time_occurrences.get((round_num, sec), False):
            heatmap_df.at[round_num, f"{sec//60}:{sec%60:02d}"] = "✅"
        else:
            heatmap_df.at[round_num, f"{sec//60}:{sec%60:02d}"] = ""

# Convert DataFrame to Dash format
heatmap_data = heatmap_df.reset_index().rename(columns={'index': 'Round'})

# Create the Dash table
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3(
        "UFC Scorigami: Fight Ending Times",
        style={'color': 'black', 'textAlign': 'center', 'fontWeight': 'bold'}
    ),
    dash_table.DataTable(
        id='scorigami-table',
        columns=[{'name': 'Round', 'id': 'Round'}] + 
                 [{'name': t, 'id': t} for t in time_labels],
        data=heatmap_data.to_dict('records'),
        style_table={'overflowX': 'auto', 'width': '100%', 'maxHeight': '500px'},
        style_header={'backgroundColor': 'lightgrey', 'fontWeight': 'bold', 'textAlign': 'center'},
        style_cell={'textAlign': 'center', 'border': '1px solid black', 'padding': '5px'},
        style_data_conditional=[
            {
                'if': {'filter_query': f'{{{t}}} eq "✅"', 'column_id': t},
                'backgroundColor': 'green',
                'color': 'green'  # Green for True values
            } for t in time_labels
        ] + [
            {
                'if': {'filter_query': f'{{{t}}} eq ""', 'column_id': t},
                'backgroundColor': 'red',
                'color': 'red'  # Red for False values
            } for t in time_labels
        ]
    )
])

# Port the Dash table to Render
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run_server(debug=True, host='0.0.0.0', port=port)

conn.close()