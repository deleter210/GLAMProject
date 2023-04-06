import json
import random

def get_random_law_text():
    law_number = random.randint(1, 118)

    with open(f'glam/greek_laws/{law_number}.json') as f:
        law_info = json.load(f)

    return law_info['content']
