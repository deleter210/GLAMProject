import re

LEGAL_KEYWORDS = {
    'Συνταγματικός': 'constitution',
    'ποινικός': 'criminal',
    'εμπορικός': 'commercial',
    'αστικός': 'civil',
    'εργατικός': 'labor',
}

SENTIMENT_KEYWORDS = {
    'θετικό': 'positive',
    'αρνητικό': 'negative',
}

LEGAL_NER_REGEX = re.compile(r'<(.*?)\|.*?>')

def process_keywords(user_input):
    extracted_keywords = extract_keywords(user_input)
    if not extracted_keywords:
        return None
    return f"I detected the following keywords in your input: {', '.join(extracted_keywords)}"

def extract_keywords(user_input):
    extracted_keywords = []
    for word in user_input.split():
        if word.lower() in LEGAL_KEYWORDS:
            extracted_keywords.append(LEGAL_KEYWORDS[word.lower()])
        elif word.lower() in SENTIMENT_KEYWORDS:
            extracted_keywords.append(SENTIMENT_KEYWORDS[word.lower()])
    return extracted_keywords

def extract_legal_ner(user_input):
    extracted_ner = []
    matches = LEGAL_NER_REGEX.findall(user_input)
    for match in matches:
        extracted_ner.append(match)
    return extracted_ner
