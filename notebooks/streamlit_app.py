import pandas as pd
import inflection
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# importar os dataframes

df_bp = pd.read_csv('data/business_performance.csv')
df_bp = df_bp.drop('Unnamed: 0', axis=1)

df_c = pd.read_csv('data/crossprice.csv')
df_c = df_c.drop('Unnamed: 0', axis=1)

df_e = pd.read_csv('data/df_elasticity.csv')

########### Layout Streamlit #############
st.set_page_config( layout='wide' )
st.header( 'Elasticidade de preços dos Produtos') 

tab1, tab2, tab3 = st.tabs( ['Elasticidade de preço dos produtos', 'Business Performance', 'Elasticidade Cruzadas de Preços'])

with tab1:
        
    st.subheader( 'Elasticidade de Preços - Gráfico' )
    df_e['ranking'] = df_e.loc[:,'price_elasticity'].rank( ascending=True ).astype( int )

    fig, ax =plt.subplots()
    plt.figure( figsize=( 12, 4 ) )
    ax.hlines(y=df_e['ranking'], xmin=0, xmax=df_e['price_elasticity'], alpha=1, linewidth=5 );

    for name, p in zip( df_e['name'], df_e['ranking'] ):
        ax.text( 4, p, name )

    for x, y, s in zip( df_e['price_elasticity'], df_e['ranking'], df_e['price_elasticity'] ):
        ax.text( x, y, round( s, 2), horizontalalignment='right' if x < 0 else 'left', 
                                    verticalalignment='center',
                                    fontdict={'color': 'red' if x < 0 else 'green', 'size': 10} )

    #ax.gca().set( ylabel='Ranking Number', xlabel='Price Elasticity' )
    #ax.title('Price Elasticity')
    ax.grid(linestyle='--')

    st.pyplot(fig)

    
    st.subheader( 'Elasticidade de Preços - DataFrame' )
    df_order_elasticity = df_e[['ranking', 'name', 'price_elasticity']].sort_values( by='price_elasticity', 
                                                                                        ascending=False)
    df_order_elasticity = df_order_elasticity.set_index('ranking')
    st.dataframe(df_order_elasticity)

with tab2:
    st.subheader('Business Performance')
    df_bp = df_bp.set_index('name')
    st.dataframe(df_bp, use_container_width=True )

with tab3:
    st.subheader('Elasticidade Cruzadas de Preços' )
    df_c = df_c.set_index('name')
    st.dataframe(df_c, use_container_width=True )