'''
- open terminal and type
- cd app2
- streamlit run app.py
'''
from turtle import width
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# STEP 1 - load the data

@st.cache
def load_data():
    weatherdf = pd.read_csv('weather.csv', parse_dates=['Date.Full'], dayfirst=True)
    # renaming cols
    weatherdf.columns = ['precipitation', 'date', 'month', 'week', 'year',
            'city', 'code', 'location', 'state', 'avg_temp', 'max_temp',
            'min_temp', 'wind_direction','wind_speed']
    # dropped cols
    weatherdf.drop(columns=['code','location'], inplace=True)
    return weatherdf

# STEP 2 - SETUP initial UI elements
st.set_page_config(
    page_title="weather analysis",
    page_icon='🌦️',
    layout='wide'
)

st.title("WEATHER ANALYSIS APP🌦️")
df = load_data()

st.sidebar.header("OPTIONS")

view_data = st.sidebar.checkbox("See raw data")
if view_data:
    st.write(df)

numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(include='object').columns.tolist()

colx = st.sidebar.selectbox("select a numerical column x", numerical_cols)
coly = st.sidebar.selectbox("select a numerical column y", numerical_cols)

graph_types = ['line','area','bar', 'scatter']
gtype = st.sidebar.radio("select a graph type", graph_types)

if gtype == graph_types[0]:
    fig = px.line(df, x=colx, y=coly)
if gtype == graph_types[1]:
    fig = px.area(df, x=colx, y=coly)
if gtype == graph_types[2]:
    fig = px.bar(df, x=colx, y=coly)
if gtype == graph_types[3]:
    fig = px.scatter(df, x=colx, y=coly)
if fig:
    st.plotly_chart(fig, use_container_width=True)

if st.sidebar.checkbox("categorical visualization"):
    catx = st.sidebar.selectbox("select category column", categorical_cols)
    numy = st.sidebar.selectbox("select numerical column", numerical_cols)
    graph_types = ['box','funnel','funnel_area']
    gtype = st.sidebar.multiselect("select a graph type", graph_types)
    limit = st.slider("Select number of rows", min_value=100, max_value=df.shape[0])
    dfc = df[:limit]
    if graph_types[0] in gtype:
        fig= px.box(dfc, x=catx, y=numy)
        st.plotly_chart(fig, use_container_width=True)
    if graph_types[1] in gtype:
        fig = px.funnel(dfc, catx, numy)
        st.plotly_chart(fig, use_container_width=True)
    if graph_types[2] in gtype:
        fig = px.funnel_area(dfc, catx, numy)
        st.plotly_chart(fig, use_container_width=True)
    