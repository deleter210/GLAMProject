import torch
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

SENTIMENT_MODEL = "kkarpou/autotrain-greek-sentiment-analysis-3351392404"
SENTIMENT_TOKENIZER = AutoTokenizer.from_pretrained(SENTIMENT_MODEL)
SENTIMENT_MODEL = AutoModelForSequenceClassification.from_pretrained(SENTIMENT_MODEL)

def analyze_sentiment(user_input):
    sentiment = pipeline(
        "text-classification",
        model=SENTIMENT_MODEL,
        tokenizer=SENTIMENT_TOKENIZER,
        device=0
    )

    result = sentiment(user_input, truncation=True)
    label = result[0]['label']
    score = result[0]['score']
    if label == 'LABEL_0':
        sentiment = 'Negative'
    elif label == 'LABEL_1':
        sentiment = 'Positive'
    else:
        sentiment = 'Neutral'
    return sentiment, score
