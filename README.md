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
<img width="1788" height="1363" alt="Screenshot 2025-11-23 164926" src="https://github.com/user-attachments/assets/6dc211fd-170d-49bd-9098-6007048cf263" />

<img width="1831" height="1414" alt="Screenshot 2025-11-23 164953" src="https://github.com/user-attachments/assets/ddfc4384-a2a4-4a92-9e4a-211d1902da85" />


<img width="1640" height="1433" alt="Screenshot 2025-11-23 165016" src="https://github.com/user-attachments/assets/607f1406-211d-4c97-9ad1-d7e0ee1fec69" />


<img width="1774" height="1343" alt="Screenshot 2025-11-23 165048" src="https://github.com/user-attachments/assets/e30b5437-f0d3-45f9-863a-66c842808572" />

