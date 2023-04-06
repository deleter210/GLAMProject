import json
from transformers import pipeline

SUMMARIZER = pipeline('summarization', model='t5-base', tokenizer='t5-base', device=0)

def get_legal_summary(law_number):
    law_info = load_law_info(law_number)
    summary = SUMMARIZER(law_info['content'], min_length=30, max_length=250)[0]['summary_text']
    return summary

def load_law_info(law_number):
    with open(f'glam/greek_laws/{law_number}.json', encoding='utf-8') as f:
        law_info = json.load(f)
    return law_info
