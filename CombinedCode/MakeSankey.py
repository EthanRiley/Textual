import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

def code_mapping(df, src, targ):
    """ map labels in src and targ columns to integers """
    labels = list(df[src]) + list(df[targ])
    #labels = sorted(list(set(labels)))
    
    #print(labels)
    
    codes = list(range(len(labels)))
    #print(codes)
    
    lcmap = dict(zip(labels, codes))
    #print(lcmap)
    
    df = df.replace({src: lcmap, targ: lcmap})
    #print(df)
    
    return df, labels


def make_sankey(df, src, targ, vals=None, filename='1', **kwargs):
    df, labels = code_mapping(df, src, targ)
    
    
    if vals:
        value = df[vals]
    else:
        value = [1] * df.shape[0]
    
    
    link = {'source':df[src], 'target':df[targ], 'value':value}
    
    pad =kwargs.get('pad', 100)
    thickness = kwargs.get('thickness', 10)
    line_color = kwargs.get('line_color', 'black')
    width = kwargs.get('width', 2)

    node = {'pad':pad, 'thickness':thickness,
            'line':{'color':line_color, 'width':width},
            'label':labels}
    
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    fig.write_image('sankey_{}.jpg'.format(filename))