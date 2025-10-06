import streamlit as st
from src.sentiment_analysis import analyze_sentiment
import time

st.set_page_config(page_title="Internship Task", page_icon="📝", layout="wide")

st.header("Internship Assessment Task")

user_input = st.text_input("Enter text for sentiment analysis", key="input_text")
analyze_button = st.button("Analyze Sentiment", key="analyze_button")

def streamer(final_response):
    """To imitate the output style of a chatbot."""
    placeholder = st.empty()
    e = ''
    for chunk in final_response:
        e += chunk
        placeholder.markdown(e)
        time.sleep(0.01)  # Simulate streaming delay
    return placeholder

col1, col2 = st.columns(2) # splits the page into two columns
with col1:
    manual_sentiment = st.checkbox("Manually select sentiment", key="manual_select")
    if manual_sentiment: # if the user checks the box, show the selectbox
        sentiment_box = st.selectbox("Select sentiment", ["Positive", "Negative", "Neutral"], index=None, key="selected_sentiment", placeholder="Select sentiment...")
with col2:
    num_words = st.slider("Select number of words", 100, 150, 100, step=10)

st.subheader("Output")
col3 = st.container(border=True) # a container for the output
with col3:
    if analyze_button and user_input: # if input is provided and button is clicked
        if manual_sentiment and sentiment_box: # if manual sentiment is selected and a sentiment is chosen
            sentiment = sentiment_box
            final_response, sentiment = analyze_sentiment(user_input, sentiment=sentiment, num_words=num_words)
            st.markdown(f"Sentiment: **{sentiment}**")
            streamer(final_response)
        else: # if manual sentiment is not selected, analyze sentiment automatically
            final_response, sentiment = analyze_sentiment(user_input, num_words=num_words)
            st.markdown(f"Sentiment: **{sentiment}**")
            streamer(final_response)