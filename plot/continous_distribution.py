
import plot
import numpy as np 
import scipy.stats as stats
import plotly.graph_objects as go 


# ========= 01. Uniform Distribution =========
def uniform_distn():
    a = 200
    b = 400
    x = np.linspace(0,800,500)
    y = stats.uniform.pdf(x,a,b)
    trace1 = go.Scatter(x=x,y=y,mode='lines',line=dict(color="green",width=3))
    layout = go.Layout(
        template="plotly_dark",
        plot_bgcolor='black',
        paper_bgcolor="black",
        title=dict(
            text="Uniform Distribution",
            font=dict(size=30,weight=500)
        ),
        xaxis=dict(title="x-axis",showgrid=False),
        yaxis=dict(title="y-axis",showgrid=False),
    )
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig 


# ========= 02. Exponential Distribution =========
def exponential_distn():
    # beta>0 
    beta = 1
    x = np.linspace(-1,6,1000)
    # x>=0 else 0 
    y = stats.expon.pdf(x,beta)
    
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=3))
    layout = go.Layout(
        template="plotly_dark",
        plot_bgcolor="black",
        paper_bgcolor="black",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        title=dict(text="Exponential Distribution",font=dict(size=30,weight=500,color="white"))
    )
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig 

# ========= 03. Gamma Distribution =========
def gamma_distn():
    alpha = 1 
    beta = 2 
    # x>0
    x = np.linspace(0.01,6,1000)
    y = stats.gamma.pdf(x,alpha,beta)
    
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(width=3,color="red"))
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        title=dict(text="Gamma Distribution",font=dict(size=30,color="white",weight=500))
    )
    
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig 

    

# ========= 04. Weibull Distribution =========
def weibull_distn():
    alpha = 2
    beta  = 3 
    #x>0 else 0 
    x = np.linspace(0.01,6,1000)
    y = stats.weibull_min.pdf(x,alpha,beta)
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=3))
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        title=dict(text="Weibull Distribution",font=dict(size=30,color="white",weight=500))
    )
    
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig 

# ========= 05. Normal Distribution =========
def normal_distn():
    mu = 0
    std  = 1
    x = np.linspace(0,600,1000)
    y = stats.norm.pdf(x,mu,std)
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=3))
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        title=dict(text="Weibull Distribution",font=dict(size=30,color="white",weight=500))
    )
    
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

# ========= 06. LogNormal Distribution =========
def log_normal_distn():
    mu = 0
    std  = 1
    # x>0 
    x = np.linspace(0.01,600,1000)
    # see the book, scale is e^mu 
    y = stats.lognorm.pdf(x,s=std,scale=np.exp(mu))
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=3))
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        title=dict(text="Weibull Distribution",font=dict(size=30,color="white",weight=500))
    )
    
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig 

# ========= 07. Beta Distribution =========
def beta_distn():
    alpha1 = 1 #>0
    alpha2  = 1 #>0
    # 1>x>0 
    x = np.linspace(0,1,1000)
    y = stats.lognorm.pdf(x,alpha1,alpha2)
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=3))
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        title=dict(text="Weibull Distribution",font=dict(size=30,color="white",weight=500))
    )
    
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig  


# ========= 08. Pearson Distribution =========
def pearson_distn():
    alpha = 1 #>0
    beta  = 1 #>0
    # x>0 
    x = np.linspace(0.01,8,1000)
    y = stats.invgamma.pdf(x,alpha,beta)
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=3))
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        title=dict(text="Weibull Distribution",font=dict(size=30,color="white",weight=500))
    )
    
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig   


# ========= 09. Log-Logistics Distribution =========
def log_logistics_distn():
    alpha1 = 1 #>0
    alpha2  = 1 #>0
    # 1>x>0 
    x = np.linspace(0,1,1000)
    y = stats.lognorm.pdf(x,alpha1,alpha2)
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=3))
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        title=dict(text="Weibull Distribution",font=dict(size=30,color="white",weight=500))
    )
    
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig   

# ========= 10. Johnson Distribution =========
def johnson_distn():
    alpha1 = 1 #>0
    alpha2  = 1 #>0
    # 1>x>0 
    x = np.linspace(0,1,1000)
    y = stats.lognorm.pdf(x,alpha1,alpha2)
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=3))
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        title=dict(text="Weibull Distribution",font=dict(size=30,color="white",weight=500))
    )
    
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig   

