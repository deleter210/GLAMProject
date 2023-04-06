import json
import random

def get_law_info(user_input):
    law_number = extract_law_number(user_input)
    if law_number:
        law_info = load_law_info(law_number)
        return format_law_info(law_info)
    return None

def random_law(user_input):
    if 'random' in user_input.lower():
        law_number = str(random.randint(1, 298))
        law_info = load_law_info(law_number)
        return format_law_info(law_info)
    return None

def get_random_law():
    law_number = str(random.randint(1, 298))
    law_info = load_law_info(law_number)
    return format_law_info(law_info)

def extract_law_number(user_input):
    for word in user_input.split():
        if word.isdigit():
            if int(word) in range(1, 299):
                return word
    return None

def load_law_info(law_number):
    with open(f'glam/greek_laws/{law_number}.json') as f:
        law_info = json.load(f)
    return law_info

def format_law_info(law_info):
    formatted_info = f"Άρθρο {law_info['article']} του Νόμου {law_info['number']} ({law_info['title']})\n\n"
    formatted_info += law_info['content']
    return formatted_info
