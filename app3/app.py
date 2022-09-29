import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import re # regular expression
from textblob import TextBlob

st.set_page_config(
    layout='wide'
)
st.title("Sentiment Analysis 🦝")

def remove_mentions(tweet):
    return re.sub('@[A-Za-z0-9_]+', "", tweet)

def remove_hashtags(tweet):
    return re.sub('#[A-Za-z0-9_]+', "", tweet)

def remove_links(tweet):
    tweet = re.sub('[()!?]',' ', tweet) # remove punc
    tweet = re.sub(r'\[.*?\]',' ', tweet) # remove punc
    tweet = re.sub(r'http\S+',' ', tweet) # remove link
    tweet = re.sub(r'www.\S+',' ', tweet) # remove link
    return re.sub(r'[^a-z0-9]',' ', tweet) # keep only alphabets and numbers

def get_sentiment(tweet):
    blob = TextBlob(tweet)
    return blob.sentiment.polarity

def get_sentiment_name(sentiment):
    if sentiment == 0:
        return "🟢 Neutral"
    elif sentiment > 0:
        return "😎 Postive"
    else:
        return "😡Negative"

@st.cache
def load_data():
    df = pd.read_csv('elonmusk.csv',
        parse_dates=['Date Created'], dayfirst=True)
    df.sort_values(by='Date Created', inplace=True)
    df['Tweets'] = df['Tweets'].str.lower()
    df['Tweets'] = df['Tweets'].apply(remove_hashtags)
    df['Tweets'] = df['Tweets'].apply(remove_mentions)
    df['Tweets'] = df['Tweets'].apply(remove_links)
    df['Sentiment'] = df['Tweets'].apply(get_sentiment)
    df['SentimentName'] = df['Sentiment'].apply(get_sentiment_name)
    return df

df = load_data()
if st.checkbox("Show raw data"):
    st.write(df)

if st.checkbox("Visualize"):
    st.header("Tweet sentiment Count")
    counter = df.SentimentName.value_counts().reset_index()
    c1, c2 = st.columns([1,3])
    c1.write(counter)
    fig = px.pie(counter,'index','SentimentName')
    c2.plotly_chart(fig, use_container_width=True)
