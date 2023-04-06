from glam.gpt_neo import GPTNeo
from glam.greek_laws import get_law_info, get_random_law
from glam.legal_info import get_legal_info
from glam.keywords import process_keywords
from glam.sentiment_analysis import analyze_sentiment
from glam.ner import get_named_entities, NER_MODEL, NER_TOKENIZER, LABELS

gpt_neo = GPTNeo()


def answer(user_input, history):
    # Check if user input contains any keywords
    keyword_response = process_keywords(user_input)
    if keyword_response:
        return keyword_response

    # Check if user input is a legal summary request
    legal_summary_response = get_legal_summary(user_input)
    if legal_summary_response:
        return legal_summary_response

    # Check if user input is a Greek law request
    law_info_response = get_law_info(user_input)
    if law_info_response:
        return law_info_response

    # Check if user input is a random Greek law request
    random_law_response = get_random_law_text(user_input)
    if random_law_response:
        return random_law_response

    # Check if user input is a legal information request
    legal_info_response = get_legal_info(user_input)
    if legal_info_response:
        return legal_info_response

    # Perform sentiment analysis on user input
    sentiment_response = analyze_sentiment(user_input)
    if sentiment_response:
        return sentiment_response

    # Perform named entity recognition on user input
    named_entities = get_named_entities(user_input)
    if named_entities:
        return named_entities

    # Use GPT-Neo to generate a response
    gpt_neo_response = gpt_neo.generate_response(history, user_input)
    return gpt_neo_response



def random_law():
    law_text = get_random_law_text()
    return f"Here's a random law for you:\n\n{law_text}"