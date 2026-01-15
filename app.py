import dash
import numpy as np 
import pandas as pd 
from dash import dcc
from dash import html
import plotly.express as px 
import plotly.graph_objects as go 
import dash_bootstrap_components as dbc 
from dash.dependencies import Input,Output


# assets->style.css (must follow this naming convention)
external_stylesheets = [
    {
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB',
        'crossorigin': 'anonymous'
    }
]


app = dash.Dash(__name__,external_stylesheets=external_stylesheets) 


# ====================Main Layout Of The Application====================
app.layout = html.Div([
    # ==== 1. Heading =====
    html.Header(" Continous Random Distribution Curve ",className="PageHeading"),

    # ================ 2. Continous Random Distribution Curve ================
    
    # === 2.1. uniform: ===
    html.Div([
        html.H2("Uniform Distribution",style={'color':'white','text-align':'center'}),
        ],className="uniform"),
    
    # === 2.2.Exponential ===
    html.Div([
        html.H2("Exponential Distribution",style={'color':'white','text-align':'center'}),
        ],className="exponential"),
    
    # === 2.3 Gamma ===
    html.Div([
        html.H2("Gamma Distribution",style={'color':'white','text-align':'center'}),
        ],className="gamma"),
    
    
    # === 2.4 Weibull ===
    html.Div([
        html.H2("Weibull Distribution",style={'color':'white','text-align':'center'}),
        ],className="weibull"),
    
    
    # === 2.5 Normal ===
    html.Div([
        html.H2("Normal",style={'color':'white','text-align':'center'}),
        ],className="normal"),
    
    
    # === 2.6 LogNormal ===
    html.Div([
        html.H2("LogNormal Distribution",style={'color':'white','text-align':'center'}),
        ],className="lognormal"),
    
    
    # === 2.7 Beta ===
    html.Div([
        html.H2("Beta Distribution",style={'color':'white','text-align':'center'}),
        ],className="beta"),
    
    
    # === 2.8 Pearson ===
    html.Div([
        html.H2("Pearson Distribution",style={'color':'white','text-align':'center'}),
        ],className="pearson"),
    
    
    # === 2.9 Log-logistics ===
    html.Div([
        html.H2("Log-Logistics",style={'color':'white','text-align':'center'}),
        ],className="logLogistics"),
    
    
    # === 2.10 Johnson ===
    html.Div([
        html.H2("Johnson",style={'color':'white','text-align':'center'}),
        ],className="johnson"),
    
    ],className="main-div"
)

# ======= For running The Application =======
if __name__=="__main__":
    app.run(debug=True)


