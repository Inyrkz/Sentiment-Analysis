# Sentiment-Analysis
This project applies both Machine Learning and Natural Language Processing to determine if the sentiment of articles, texts, comments in a website is positive, neutral or negative.

The libraries need to run this project are in the `requirements.txt` file.
You can install them by running the code below in your terminal.

```python
pip install -r requirements.txt
```
The python script for creating the sentiment analysis model is `sentiment.py`.
The flask rest api script is `app.py`.

To create the pickled model, run the sentiment.py script in your terminal
```python
python sentiment.py
```

To run the flask api locally, run the code below in your terminal
```python
python app.py
```
