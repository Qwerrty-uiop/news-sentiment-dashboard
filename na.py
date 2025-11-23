# news_analysis.py

import requests
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    print("VADER lexicon not found. Downloading...")
    nltk.download('vader_lexicon')

API_KEY = "102b93cb6d7d472bb9543c9d26b15e6e" 

def fetch_news(topic):
    """Fetches a list of news headlines for a given topic."""
    url = (f"https://newsapi.org/v2/everything?q={topic}"
           f"&language=en&sortBy=relevancy&pageSize=30&apiKey={API_KEY}")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        headlines = [article['title'] for article in data.get('articles', []) if article['title']]
        return headlines
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return []

def analyze_sentiment(text):
    """Analyzes the sentiment of a piece of text using VADER."""
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

