
import plot
import numpy as np 
import scipy.stats as stats
import plotly.graph_objects as go 


# ========= 01. Uniform Distribution =========
def uniform_distn(a=100,b=200):
    x = np.linspace(0,800,500)
    y = stats.uniform.pdf(x,a,(b-a))
    trace1 = go.Scatter(x=x,y=y,mode='lines',line=dict(color="red",width=6),name=f"a:{a}, b:{b}, b-a: {b-a}")
    layout = go.Layout(
        template="plotly_dark",
        plot_bgcolor='black',
        paper_bgcolor="black",
        # title=dict(
        #     text="Uniform Distribution",
        #     font=dict(size=30,weight=500)
        # ),
        legend=dict(font=dict(size=20)),
        xaxis=dict(title="x-axis",showgrid=False),
        yaxis=dict(title="y-axis",showgrid=False),
        showlegend=True
    )
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig 



# ========= 02. Exponential Distribution =========
def exponential_distn(beta):
    # beta>0 
    #beta = 1
    x = np.linspace(-1,10,1000)
    # x>=0 else 0 
    y = stats.expon.pdf(x,beta)
    
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=6),name=f"beta: {beta}")
    layout = go.Layout(
        template="plotly_dark",
        plot_bgcolor="black",
        paper_bgcolor="black",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        #title=dict(text="Exponential Distribution",font=dict(size=30,weight=500,color="white"))
        legend=dict(font=dict(size=20)),
        showlegend=True
    )
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig 



# ========= 03. Gamma Distribution =========
def gamma_distn(alpha,beta):
    # alpha = 1 #>0
    # beta = 2 #>0
    
    # x>0
    x = np.linspace(0.01,10,1000)
    y = stats.gamma.pdf(x,alpha,beta)
    
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(width=6,color="red"),name=f"alpha: {alpha} beta: {beta}")
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        #title=dict(text="Gamma Distribution",font=dict(size=30,color="white",weight=500))
        legend=dict(font=dict(size=20)),
        showlegend=True
    )
    
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig 

    


# ========= 04. Weibull Distribution =========
def weibull_distn(alpha,beta):
    # alpha = 2 #>0
    # beta  = 3 #>0
    
    #x>0 else 0 
    x = np.linspace(0.01,6,1000)
    y = stats.weibull_min.pdf(x,alpha,beta)
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=6),name=f"alpha: {alpha}, beta: {beta}")
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        #title=dict(text="Weibull Distribution",font=dict(size=30,color="white",weight=500))
        legend=dict(font=dict(size=20)),
        showlegend=True
    )
    
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig 



# ========= 05. Normal Distribution =========
def normal_distn(mu=100,std=20):
    x = np.linspace(0,600,1000)
    y = stats.norm.pdf(x,mu,std)
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=6),name=f"mu: {mu}, std: {std}")
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        #title=dict(text="Normal Distribution",font=dict(size=30,color="white",weight=500))
        legend=dict(font=dict(size=20)),
        showlegend=True
    )
    
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    



# ========= 06. LogNormal Distribution =========
def log_normal_distn(std,emu):
    # mu = 1>0
    # std  = 1>0
    
    # x>0 
    x = np.linspace(0.01,10,1000)
    
    # see the book, scale is e^mu 
    y = stats.lognorm.pdf(x,s=std,scale=np.exp(emu))
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=6),name=f"mu: {std}, e^mu: {emu}")
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        #title=dict(text="LogNormal Distribution",font=dict(size=30,color="white",weight=500))
        legend=dict(font=dict(size=20)),
        showlegend=True
    )
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig 



# ========= 07. Beta Distribution =========
def beta_distn(alpha1,alpha2):
    # alpha1 = 1 #>0
    # alpha2  = 1 #>0
    
    # 1>x>0 
    x = np.linspace(0.001,1,1000)
    y = stats.beta.pdf(x,alpha1,alpha2)
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=6),name=f"alpha1: {alpha1}, alpha2: {alpha2}")
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        #title=dict(text="Beta Distribution",font=dict(size=30,color="white",weight=500))
        legend=dict(font=dict(size=20)),
        showlegend=True
    )
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig  


# ========= 08. Pearson Distribution =========
def pearson_distn(alpha,beta):
    # alpha = 1 #>0
    # beta  = 1 #>0
    
    # x>0 
    x = np.linspace(0.01,8,1000)
    y = stats.invgamma.pdf(x,alpha,beta)
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=6),name=f"alpha: {alpha}, beta: {beta}")
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        #title=dict(text="Pearson Distribution",font=dict(size=30,color="white",weight=500))
        legend=dict(font=dict(size=20)),
        showlegend=True
    )
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig   


# ========= 09. Log-Logistics Distribution =========
def log_logistics_distn(alpha,beta):
    # alpha = 1 # >0
    # beta = 2 #>0
    
    # x>0 
    x = np.linspace(0.001,6,1000)
    
    # scipy use one parameter: 
    y = stats.fisk.pdf(x,alpha,scale=beta)
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=6),name=f"alpha: {alpha}, beta: {beta}")
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        #title=dict(text="LogLogistics Distribution",font=dict(size=30,color="white",weight=500))
        legend=dict(font=dict(size=20)),
        showlegend=True
    )
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig   

# ========= 10. Johnson^B Distribution =========
def johnson_distn(alpha1,alpha2,a,b):
    # alpha1 = 0 # (-inf,inf)
    # alpha2  = 2 # >0 
    # a = 0 
    # b = 2 
    
    # a<x<b: 
    x = np.linspace(a+0.001,b-0.001,1000)
    y = stats.johnsonsb.pdf(x,alpha1,alpha2,loc=a,scale=(b-a))
    trace1 = go.Scatter(x=x,y=y,mode="lines",line=dict(color="red",width=6),
                        name=f"alpha1: {alpha1}, alpha2: {alpha2}, a: {a}, b: {b}")
    layout = go.Layout(
        template="plotly_dark",
        xaxis=dict(title="xaxis",showgrid=False),
        yaxis=dict(title="yaxis",showgrid=False),
        plot_bgcolor="black",
        paper_bgcolor="black",
        #title=dict(text="JohnsonB Distribution",font=dict(size=30,color="white",weight=500))
        legend=dict(font=dict(size=20)),
        showlegend=True
    )
    trace = [trace1]
    fig = go.Figure(data=trace,layout=layout)
    return fig   

