import dash
import dash_core_components as dcc
import dash_html_components as html
import sys
import requests

def get_plot_data(raw_data):
    data=raw_data["data"]
    totalcases={'name':'total_cases','x':[],'y':[],'type':'line'}
    recovered={'name':'recovered','x':[],'y':[],'type':'line'}
    active={'name':'active_cases','x':[],'y':[],'type':'line'}
    deceased={'name':'deceased','x':[],'y':[],'type':'line'}
    for d in data:
        #print(d["summary"])
        totalcases['x'].append(d["day"])
        totalcases['y'].append(d["summary"]["total"])
        recovered['x'].append(d["day"])
        recovered['y'].append(d["summary"]["discharged"])
        active['x'].append(d["day"])
        active['y'].append(d["summary"]["total"]-d["summary"]["discharged"])
        deceased['x'].append(d["day"])
        deceased['y'].append(d["summary"]["deaths"])
    live_data=[totalcases,recovered,active,deceased]
    
    return live_data





app=dash.Dash()

raw_data=requests.get("https://api.rootnet.in/covid19-in/stats/history").json()
live_data = get_plot_data(raw_data)

app.layout = html.Div(children=[
    html.H1(children='Live covid 19 India',
            style={'textAlign':'center','color':'#7FDBFE'}
            ),
    dcc.Graph(id='covid19',
              figure={
                  'data':live_data,
                  'layout':{
                      'title':'live trend',
                      'plot_bgcolor': '#111111',
                    'paper_bgcolor': '#111111',
                    'font': {
                    'color': '#7FDBFF'
                        }
                  }
              }

    )
],style={'backgroundColor': '#111111'})



if __name__=='__main__':
    app.run_server(debug=True)