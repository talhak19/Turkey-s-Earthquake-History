import plotly.express as px
import pandas as pd



def show_graphics(data):
    #Yıllık deprem dağılımları
    fig_hist = px.histogram(data_frame=data, x='Olus zamani')
    fig_hist.update_layout(title_text='Distribution of the Earthquakes (Annually)',
                        title_x=0.5, title_font=dict(size=32))
    fig_hist.update_traces(marker=dict(line=dict(color='#000000', width=2)))
    fig_hist.show()
    
    #Deprem büyüklükleri dağılımları
    fig = px.histogram(data, x="xM", marginal='rug', hover_data=data.columns)
    fig.update_layout(title_text='Distribution of the Magnitudes',
                    title_x=0.5, title_font=dict(size=32))
    fig.show()    

    #Deprem lokasyonları dağılımları
    Yer_count = data.groupby(pd.Grouper(key='Yer')).size().reset_index(name='count')
    fig = px.treemap(Yer_count, path=['Yer'], values='count')
    fig.update_layout(title_text='Number of Earthquakes due to Location',
                    title_x=0.5, title_font=dict(size=30)
                    )
    fig.update_traces(textinfo="label+value")
    fig.show()