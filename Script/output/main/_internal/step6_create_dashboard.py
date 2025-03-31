import pandas as pd
import datetime as dt
from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output

#final data
file_path = 'Researcher_Assigned_Calls_With_Deadline_URL.xlsx'
data = pd.read_excel(file_path)

#convert 'Deadline' column to datetime and filter out past deadlines
data['Deadline'] = pd.to_datetime(data['Deadline'], format='%d %m %Y').dt.date
today = dt.date.today()
data = data[data['Deadline'] >= today]  #filter out past deadlines
data = data.sort_values(by='Deadline').reset_index(drop=True)

#function to assign row color based on deadline
def assign_color(deadline_date, today=today):
    days_until_deadline = (deadline_date - today).days
    if days_until_deadline <= 10:
        return 'red'  #urgent
    elif days_until_deadline <= 30:
        return 'yellow'  #close
    else:
        return 'green'  #plenty of time

data['Row_Color'] = data['Deadline'].apply(assign_color)

data['URL'] = data['URL'].apply(lambda x: f"[Link]({x})")

data['Formatted_Deadline'] = data['Deadline'].apply(lambda x: x.strftime('%d-%m-%Y'))

app = Dash(__name__)

style_conditions = [
    {
        'if': {'filter_query': '{Row_Color} = "red"'},
        'backgroundColor': 'tomato',
        'color': 'white'
    },
    {
        'if': {'filter_query': '{Row_Color} = "yellow"'},
        'backgroundColor': 'gold',
        'color': 'black'
    },
    {
        'if': {'filter_query': '{Row_Color} = "green"'},
        'backgroundColor': 'lightgreen',
        'color': 'black'
    }
]

#app layout
app.layout = html.Div([
    html.Div([
        html.H1("Funding Calls Dashboard", style={
            'text-align': 'center', 'color': '#2E4053', 'padding': '10px',
            'font-family': 'Arial, sans-serif', 'text-shadow': '1px 1px 2px #000',
            'margin-top': '20px', 'border': 'none', 'box-shadow': 'none'
        }),

        html.Div([
            dcc.Input(
                id='professor-search',
                type='text',
                placeholder="🔍 Enter Name",
                style={'width': '100%', 'max-width': '600px', 'padding': '10px',
                       'border': '2px solid #ccc', 'border-radius': '12px',
                       'box-shadow': '0px 4px 8px rgba(0,0,0,0.2)', 'font-size': '16px',
                       'margin': '10px auto'}
            ),
        ], style={'display': 'flex', 'justify-content': 'center', 'padding-bottom': '20px'}),

        html.Div([
            dash_table.DataTable(
                id='calls-table',
                columns=[
                    {'name': 'Researcher', 'id': 'Full Name'},
                    {'name': 'Project Name', 'id': 'Assigned Call'},
                    {'name': 'Deadline', 'id': 'Formatted_Deadline'},
                    {'name': 'URL', 'id': 'URL', 'presentation': 'markdown'},
                ],
                data=data.to_dict('records'),
                style_data_conditional=style_conditions,
                style_table={'width': '100%', 'max-width': '1200px', 'margin': '0 auto', 'border-radius': '12px', 'overflow': 'hidden'},
                
                style_cell={'textAlign': 'center', 'padding': '15px',
                            'font-family': 'Arial, sans-serif', 'border': '1px solid #ddd',
                            'whiteSpace': 'normal', 'height': 'auto', 'minWidth': '130px'},
                style_header={'backgroundColor': 'rgba(46, 64, 83, 0.8)', 'fontWeight': 'bold',
                              'color': 'white', 'text-align': 'center', 'border': '1px solid #2E4053'},
                markdown_options={'link_target': '_blank'}
            )
        ], style={'margin': '20px auto', 'width': '90%', 'max-width': '1200px', 'padding': '37px', 'border-radius': '12px',
                  'background-color': 'rgba(255, 255, 255, 0.8)', 'box-shadow': '0px 8px 16px rgba(0,0,0,0.2)'})
    ])
], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'flex-direction': 'column',
          'background-image': 'url("/assets/background.jpg")', 'background-size': 'cover',
          'background-position': 'center', 'background-attachment': 'fixed', 'padding-top': '60px',
          'padding-bottom': '60px', 'width': '100vw', 'min-height': '100vh', 'box-sizing': 'border-box',
          'overflow': 'auto'})

@app.callback(
    Output('calls-table', 'data'),
    Input('professor-search', 'value')
)
def update_table(professor_name):
    if professor_name:
        filtered_data = data[data['Full Name'].str.contains(professor_name, case=False, na=False)]
    else:
        filtered_data = data
    return filtered_data.to_dict('records')

# Run the app
if __name__ == '__main__':
    #this debug statement might break dash. either downgrade dash or change this statement to app.run()
    app.run_server(debug=True)
