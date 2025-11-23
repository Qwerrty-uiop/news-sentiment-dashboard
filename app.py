# app.py

import streamlit as st
import na

# ===================================================================
# Page Configuration
# ===================================================================

# Setting the title and an icon
st.set_page_config(page_title="News Sentiment Dashboard", page_icon="📰")

# ===================================================================
# Header Section
# ===================================================================

# Display the main title and a subtitle
st.title("📰 News Sentiment Dashboard")
st.write(
    "Enter any topic (like 'Bitcoin', 'NVIDIA', or 'SpaceX') to fetch and "
    "analyze the sentiment of the latest news headlines."
)

# ===================================================================
# Main Application Logic
# ===================================================================

# Create a text input box for the user to enter their topic
user_topic = st.text_input("Enter a Topic:")

# Create a button that the user will click to start the analysis
if st.button("Analyze Sentiment"):
    
    # We use .strip() to remove any accidental spaces
    clean_topic = user_topic.strip()
    
    if clean_topic:
        with st.spinner(f"Fetching and analyzing news for '{clean_topic}'..."):
            
            # --- This is the first connection to our engine! ---
            headlines = na.fetch_news(clean_topic)
            
            if not headlines:
                st.error("Could not fetch any headlines. Please check the topic or your API key in na.py.")
            else:
                # Create lists to hold the results
                sentiments = []
                positive_headlines = []
                negative_headlines = []
                neutral_headlines = []
                
                # --- This is the second connection to our engine! ---
                for h in headlines:
                    sentiment = na.analyze_sentiment(h)
                    sentiments.append(sentiment)
                    if sentiment == "Positive":
                        positive_headlines.append(h)
                    elif sentiment == "Negative":
                        negative_headlines.append(h)
                    else:
                        neutral_headlines.append(h)

                # --- Displaying the Results ---
                
                # 1. Show the overall summary chart
                st.subheader("Sentiment Analysis Summary")
                sentiment_counts = {
                    "Positive": sentiments.count("Positive"),
                    "Negative": sentiments.count("Negative"),
                    "Neutral": sentiments.count("Neutral")
                }
                st.bar_chart(sentiment_counts)

                # 2. Show the headlines, sorted into expandable sections
                st.subheader("Analyzed Headlines")

                with st.expander(f"🟢 Positive Headlines ({len(positive_headlines)})"):
                    for h in positive_headlines:
                        st.success(h)
                
                with st.expander(f"🔴 Negative Headlines ({len(negative_headlines)})"):
                    for h in negative_headlines:
                        st.error(h)
                        
                with st.expander(f"⚪ Neutral Headlines ({len(neutral_headlines)})"):
                    for h in neutral_headlines:
                        st.info(h)
    else:
        st.warning("Please enter a topic to analyze.")