import dash
import numpy as np 
import pandas as pd 
from dash import dcc
from dash import html
import plotly.express as px 
import plotly.graph_objects as go 
import dash_bootstrap_components as dbc 
import plot.continous_distribution as cd 
from dash.dependencies import Input,Output


# # assets->style.css (must follow this naming convention)
# external_stylesheets = [
#     {
#         'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css',
#         'rel': 'stylesheet',
#         'integrity': 'sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB',
#         'crossorigin': 'anonymous'
#     }
# ]

external_stylesheets = [dbc.themes.BOOTSTRAP] 

def create_slider_row(label, slider_id, min_val, max_val, step, value, marks_step=60):
    return html.Div([
            html.Label(f'{label}:', style={'color': 'light-gray', 'width': '100px', 'fontWeight': 'bold'}),
            html.Div(
                dcc.Slider(
                    id=slider_id,
                    min=min_val,
                    max=max_val,
                    step=step,
                    value=value,
                    marks={i: {'label': str(i), 'style': {'color': 'purple'}} for i in range(min_val, max_val+1, marks_step)},
                    tooltip={'placement': 'bottom','always_visible': True,'style':{'color':'purple'}}
                ), style={'flex-grow': '1'} 
            )
        ], style={
            'display': 'flex', 
            'flexDirection': 'row', 
            'alignItems': 'center',
            'width': '80%', 
            'margin': '0 auto 40px auto',
            'padding': '10px',
            'color':'light-gray'
        })
    
    
    
app = dash.Dash(__name__,external_stylesheets=external_stylesheets) 


# ====================Main Layout Of The Application====================
app.layout = html.Div([
    # ==== 1. Heading =====
    html.Header(" Continous Random Distribution Curve ",className="PageHeading",style={'color':'orange'}),

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # ********************************************************************************************
    # ==================== 2. Continous Random Distribution Curve ================================
    # ********************************************************************************************
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # === 2.1. uniform: ===
    html.Div([
        html.H2("Uniform Distribution",style={'color':'Purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Value of B must be greater than A**. If not then b = a+b . 
                         """,style={"color":"light-gray"}),
            create_slider_row(label="Value of A: ",slider_id="a_slider_uniform",min_val=0,max_val=800,step=50,value=200,marks_step=1),
            create_slider_row(label="Value of B: ",slider_id="b_slider_uniform",min_val=0,max_val=800,step=50,value=600,marks_step=1),
            dcc.Graph(id="id_uniform")
        ])
        ],className="uniform"),
    
    # === 2.2.Exponential ===
    html.Div([
        html.H2("Exponential Distribution",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Scale Parameter Beta where, Beta>0**""",style={"color":"light-gray"}),
            create_slider_row(label="Beta : ",slider_id="beta_slider_exponential",min_val=0,max_val=10,step=1,value=5,marks_step=1),
            dcc.Graph(id="id_exponential")
        ])
        ],className="exponential"),
    
    
    # === 2.3 Gamma ===
    html.Div([
        html.H2("Gamma Distribution",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Shape Parameter Alpha(α) where, α>0 and Scale Parameter Beta(β) where, β>0**. If not then alpha+=1 also beta+=1 """,style={"color":"light-gray"}),
            dcc.Markdown("""- For shape parameter alpha = 1 ,it becomes a exponential distribution.
                         """,style={"color":"light-gray"}),
            create_slider_row(label="Alpha: ",slider_id="alpha_slider_gamma",min_val=0,max_val=10,step=1,value=2,marks_step=1),
            create_slider_row(label="Beta: ",slider_id="beta_slider_gamma",min_val=0,max_val=10,step=50,value=3,marks_step=1),
            dcc.Graph(id="id_gamma")
        ])
        ],className="gamma"),
    
    
    # === 2.4 Weibull ===
    html.Div([
        html.H2("Weibull Distribution",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Shape Parameter Alpha(α) where, α>0 and Scale Parameter Beta(β) where, β>0**. If not then alpha+=1 also beta+=1 """,
                        style={"color":"light-gray"}),
            dcc.Markdown("""- For shape parameter alpha = 1 ,it becomes a exponential distribution.
                         """,style={"color":"light-gray"}),
            create_slider_row(label="Alpha: ",slider_id="alpha_slider_weibull",min_val=0,max_val=10,step=1,value=3,marks_step=1),
            create_slider_row(label="Beta: ",slider_id="beta_slider_weibull",min_val=0,max_val=10,step=1,value=3,marks_step=1),
            dcc.Graph(id="id_weibull")
        ])
        ],className="weibull"),
    

    # === 2.5 Normal ===
    html.Div([
        html.H2("Normal", style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Location Parameter(μ) , Scale Parameter (σ)**""",
                        style={"color":"light-gray"}),
            create_slider_row(label='Mean (μ)', slider_id='mu_slider_normal', min_val=0, max_val=600, step=10,value=300,marks_step=30),
            create_slider_row(label='Std (σ)',slider_id='std_slider_normal',min_val=0,max_val=600,step=10,value=20,marks_step=30),
            dcc.Graph(id="id_normal"),
        ]),
    ], className="normal"),
    
    
    
    # === 2.6 LogNormal ===
    html.Div([
        html.H2("LogNormal Distribution",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Shape Parameter(σ)> 0 , Scale Parameter e^{μ}>0 **""",
                        style={"color":"light-gray"}),
            create_slider_row(label='Shape (σ)',slider_id='std_slider_lognormal',min_val=0,max_val=10,step=0.1,value=0.4,marks_step=1),
            create_slider_row(label='Scale (e^μ)', slider_id='emu_slider_lognormal', min_val=0, max_val=10, step=0.1,value=1,marks_step=1),
            dcc.Graph(id="id_lognormal")
        ])
        ],className="lognormal"),
    
    
    
    # === 2.7 Beta ===
    html.Div([
        html.H2("Beta Distribution",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Shape Parameter α1 and α2 both must be greater than 0. And 0<x<1**""",
                        style={"color":"light-gray"}),
            create_slider_row(label='alpha1 (α1)',slider_id='alpha1_slider_beta',min_val=0,max_val=10,step=0.1,value=5,marks_step=1),
            create_slider_row(label='alpha2 (α2)', slider_id='alpha2_slider_beta', min_val=0, max_val=10, step=0.1,value=1.5,marks_step=1),
            dcc.Graph(id="id_beta")
        ])
        ],className="beta"),
    
    
    # === 2.8 Pearson ===
    html.Div([
        html.H2("Pearson-V Distribution",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Shape Parameter Alpha(α) where, α>0 and Scale Parameter Beta(β) where, β>0**. If not then alpha+=1 also beta+=1 """,
                        style={"color":"light-gray"}),
            create_slider_row(label="Alpha: ",slider_id="alpha_slider_pearson_v",min_val=0,max_val=10,step=0.1,value=3,marks_step=1),
            create_slider_row(label="Beta: ",slider_id="beta_slider_pearson_v",min_val=0,max_val=10,step=0.1,value=3,marks_step=1),
            dcc.Graph(id="id_pearson")
        ])
        ],className="pearson"),
    
    
    # === 2.9 Log-logistics ===
    html.Div([
        html.H2("Log-Logistics",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Shape Parameter Alpha(α) where, α>0 and Scale Parameter Beta(β) where, β>0**. If not then alpha+=1 also beta+=1 """,
                        style={"color":"light-gray"}),
            create_slider_row(label="Alpha: ",slider_id="alpha_slider_loglogistics",min_val=0,max_val=10,step=0.1,value=3,marks_step=1),
            create_slider_row(label="Beta: ",slider_id="beta_slider_loglogistics",min_val=0,max_val=10,step=0.1,value=3,marks_step=1),
            dcc.Graph(id="id_loglogistics")
        ])
        ],className="logLogistics"),
    
    
    # === 2.10 Johnson S_B ===
    html.Div([
        html.H2("Johnson Sb",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Location Parameter, a(-inf,inf), Scale Parameter (b-a), Shape Parameter α1(-inf,inf) and α2> 0. And a<x<b**""",
                        style={"color":"light-gray"}),
            create_slider_row(label="Value of A: ",slider_id="a_slider_jhonson",min_val=-10,max_val=10,step=1,value=1,marks_step=1),
            create_slider_row(label="Value of B: ",slider_id="b_slider_jhonson",min_val=-10,max_val=10,step=1,value=3,marks_step=1),
            create_slider_row(label="Alpha: ",slider_id="alpha1_slider_jhonson",min_val=-10,max_val=10,step=1,value=3,marks_step=1),
            create_slider_row(label="Beta: ",slider_id="alpha2_slider_jhonson",min_val=0,max_val=20,step=1,value=4,marks_step=1),
            dcc.Graph(id="id_jhonson")
        ])
        ],className="johnson"),
    
    
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    # ============================================================================================
    # ********************************************************************************************
    # ==================== 3. Discreate Random Distribution Curve ================================
    # ********************************************************************************************
    # ============================================================================================
    # $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    
    # ==== 1. Heading =====
    html.Header(" Discreate Random Distribution Curve ",
                className="PageHeading",style={'color':'orange'}),

    # ------------ 3.1 Bernoulli Distribution -----------------
    html.Div([
        html.H2("Bernoulli Distribution",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Here, x is the number of input. For that we will calculate probabilty(p).**""",
                        style={"color":"light-gray"}),
            create_slider_row(label="(x): ",slider_id="x_slider_bernoulli",min_val=0,max_val=500,step=10,value=50,marks_step=50),
            dcc.Graph(id="id_bernoulli")
        ])
        ],className="bernoulli"),
    
    
    # ------------ 3.2 Binomial Distribution -----------------
    html.Div([
        html.H2("Binomial Distribution",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Here, n is the number of trials and p is the probability of true.**""",
                        style={"color":"light-gray"}),
            create_slider_row(label="Number of trials(n): ",slider_id="n_slider_binomial",min_val=0,max_val=500,step=10,value=50,marks_step=50),
            create_slider_row(label="Probability of true(p): ",slider_id="p_slider_binomial",min_val=0,max_val=1,step=0.1,value=0.5,marks_step=1),
            dcc.Graph(id="id_binomial")
        ])
        ],className="boinomial"),
    
    
    # ------------ 3.3 Descreate Uniform Distribution -----------------
    html.Div([
        html.H2("Descreate Uniform Distribution",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Location Parameter, a(-inf,inf), Scale Parameter (b-a), Shape Parameter α1(-inf,inf) and α2> 0. And a<x<b**""",
                        style={"color":"light-gray"}),
            dcc.Graph(id="id_descreateuniform")
        ])
        ],className="descreateUniform"),
    
    
    # ------------ 3.4 Poisson  Distribution -----------------
    html.Div([
        html.H2("Poisson Distribution",style={'color':'purple','text-align':'center'}),
        html.Div([
            dcc.Markdown("""**Location Parameter, a(-inf,inf), Scale Parameter (b-a), Shape Parameter α1(-inf,inf) and α2> 0. And a<x<b**""",
                        style={"color":"light-gray"}),
            dcc.Markdown("""- Where number of trials(n) is high.""",style={"color":"light-gray"}),
            dcc.Markdown("""- Where probability(p) of success is very very low.""",style={"color":"light-gray"}),
            dcc.Markdown("""- Where mean or lamda(λ) = n * p .""",style={"color":"light-gray"}),
            dcc.Markdown("""- A company makes light. Intentionally that company will not make defective light. 
                         If we assume sucess as finding defective light then there we will use Poission Distribution.""",
                         style={"color":"light-gray"}),
            create_slider_row(label="Value of X: ",slider_id="x_slider_poisson",min_val=0,max_val=50,step=10,value=10,marks_step=5),
            create_slider_row(label="Value of Lamda: ",slider_id="lamda_slider_poisson",min_val=0,max_val=10,step=0.1,value=10,marks_step=1),
            dcc.Graph(id="id_poisson")
        ])
        ],className="poisson"),
    
    ],className="main-div"
)



#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# ======================================= CallBacks ======================================
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# =========================1. Callbacks for Uniform Distribution=========================
@app.callback(Output(component_id='id_uniform',component_property='figure'),
              [Input(component_id="a_slider_uniform",component_property="value"),
               Input(component_id='b_slider_uniform',component_property='value')])
def update_uniform(a_val,b_val):
    if b_val<a_val:
        b_val += a_val
    return cd.uniform_distn(a_val,b_val)


# =========================2. Callbacks for exponential Distribution=========================
@app.callback(Output(component_id='id_exponential',component_property='figure'),
              [Input(component_id="beta_slider_exponential",component_property="value")])
def update_exponential(beta_val):
    if beta_val==0:
        beta_val = beta_val+1 
    return cd.exponential_distn(beta_val)


# =========================3. Callbacks for gamma Distribution=========================
@app.callback(Output(component_id='id_gamma',component_property='figure'),
              [Input(component_id="alpha_slider_gamma",component_property="value"),
               Input(component_id="beta_slider_gamma",component_property="value")])
def update_gamma(alpha,beta):
    if alpha==0:
        alpha += 1
    if beta==0:
        beta += 1
    return cd.gamma_distn(alpha,beta)


# =========================4. Callbacks for weibull Distribution=========================
@app.callback(Output(component_id='id_weibull',component_property='figure'),
              [Input(component_id="alpha_slider_weibull",component_property="value"),
               Input(component_id="beta_slider_weibull",component_property="value")])
def update_weibull(alpha,beta):
    if alpha==0:
        alpha += 1
    if beta==0:
        beta += 1
    return cd.weibull_distn(alpha,beta)


# =========================5. Callbacks for Normal Distribution=========================
@app.callback(Output(component_id="id_normal",component_property='figure'),
              [Input(component_id="mu_slider_normal",component_property="value"),
               Input(component_id="std_slider_normal",component_property="value")])
def update_normal(mu_val,std_val):
    if std_val==0:
        std_val = 0.001
    return cd.normal_distn(mu=mu_val,std=std_val)



# =========================6. Callbacks for Log-Normal Distribution=========================
@app.callback(Output(component_id="id_lognormal",component_property='figure'),
              [Input(component_id="std_slider_lognormal",component_property="value"),
               Input(component_id="emu_slider_lognormal",component_property="value")])
def update_lognormal(std,mu):
    if mu==0:
        mu = 1 
    if std==0:
        std = 1
    return cd.log_normal_distn(std,mu)



# =========================7. Callbacks for  Beta Distribution=========================
@app.callback(Output(component_id="id_beta",component_property='figure'),
              [Input(component_id="alpha1_slider_beta",component_property="value"),
               Input(component_id="alpha2_slider_beta",component_property="value")])
def update_beta(alpha1,alpha2):
    if alpha1==0:
        alpha1+=1 
    if alpha2==0:
        alpha2+=1
    return cd.beta_distn(alpha1,alpha2)


# =========================8. Callbacks for Pearson-Type-V Distribution=========================
@app.callback(Output(component_id='id_pearson',component_property='figure'),
              [Input(component_id="alpha_slider_pearson_v",component_property="value"),
               Input(component_id="beta_slider_pearson_v",component_property="value")])
def update_pearson(alpha,beta):
    if alpha==0:
        alpha += 1
    if beta==0:
        beta += 1
    return cd.pearson_distn(alpha,beta)

# =========================9. Callbacks for LogLogistics Distribution=========================
@app.callback(Output(component_id='id_loglogistics',component_property='figure'),
              [Input(component_id="alpha_slider_loglogistics",component_property="value"),
               Input(component_id="beta_slider_loglogistics",component_property="value")])
def update_loglogistics(alpha,beta):
    if alpha==0:
        alpha += 1
    if beta==0:
        beta += 1
    return cd.log_logistics_distn(alpha,beta)



# =========================10. Callbacks for JonsonSb Distribution=========================
@app.callback(Output(component_id='id_jhonson',component_property='figure'),
              [Input(component_id="a_slider_jhonson",component_property="value"),
               Input(component_id="b_slider_jhonson",component_property="value"),
               Input(component_id="alpha1_slider_jhonson",component_property="value"),
               Input(component_id="alpha2_slider_jhonson",component_property="value")])
def update_jonsonsb(a,b,alpha1,alpha2):
    if b<a:
        b = a+b 
    if alpha2==0:
        alpha += 1
    return cd.johnson_distn(alpha1,alpha2,a,b)





# =========================================================================================
# =========================================================================================
# ============================Discreate Random Variables ==================================
# =========================================================================================
# =========================================================================================

# =========================1. Callbacks for Bernoulli=========================
@app.callback(Output(component_id='id_bernoulli',component_property='figure'),
              [Input(component_id="x_slider_bernoulli",component_property="value")])
def update_bernoulli(x):
    return cd.bernoulli_distn(x)


# =========================2. Callbacks for Binomial=========================
@app.callback(Output(component_id='id_binomial',component_property='figure'),
              [Input(component_id="n_slider_binomial",component_property="value"),
               Input(component_id="p_slider_binomial",component_property="value")])
def update_binomial(n,p):
    return cd.binomial_distn(n=n,p=p)

# =========================4. Callbacks for Poisson=========================
@app.callback(Output(component_id='id_poisson',component_property='figure'),
              [Input(component_id="x_slider_poisson",component_property="value"),
               Input(component_id="lamda_slider_poisson",component_property="value")])
def update_binomial(n,lamda):
    return cd.poisson_distn(n,lamda)

# for hosting:

server = app.server

# ======= For running The Application =======
if __name__=="__main__":
    app.run(debug=True)


