\# News Sentiment Dashboard



\## Overview of the project

This project is a web-based dashboard that fetches live news headlines from around the world on any given topic. It then uses a Natural Language Processing (NLP) model to perform sentiment analysis on each headline, classifying it as Positive, Negative, or Neutral. The results are presented in a clean, interactive interface with a visual summary chart.



\## Features

\- \*\*Live News Fetching:\*\* Retrieves the latest news on any user-defined topic using the NewsAPI.

\- \*\*Advanced Sentiment Analysis:\*\* Utilizes the VADER (Valence Aware Dictionary and sEntiment Reasoner) model, which is specifically tuned for news and social media text, providing more nuanced analysis than simpler models.

\- \*\*Interactive Dashboard:\*\* A user-friendly web interface built with Streamlit.

\- \*\*Visual Summary:\*\* Displays a bar chart summarizing the overall sentiment distribution for the topic.

\- \*\*Organized Results:\*\* Headlines are sorted into color-coded, expandable sections for easy reading.



\## Technologies/tools used

\- \*\*Backend:\*\* Python

\- \*\*Web Framework:\*\* Streamlit

\- \*\*NLP Library:\*\* NLTK with the VADER sentiment analysis engine.

\- \*\*API:\*\* NewsAPI.org for live news data.

\- \*\*Data Handling:\*\* `requests` library for API calls.



\## Steps to install \& run the project

1\.  Clone the repository.

2\.  Install the required packages: `pip install -r requirements.txt`

3\.  Run the application: `streamlit run app.py`



\## Screenshots

