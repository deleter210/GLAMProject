import json

def load_legal_info(info_type):
    with open(f'glam/legal_info/{info_type}.json') as f:
        legal_info = json.load(f)
    return legal_info

def get_legal_info(info_type, category=None):
    legal_info = load_legal_info(info_type)
    if category:
        if category in legal_info:
            return format_legal_info(legal_info[category])
        return None
    else:
        return legal_info.keys()

def format_legal_info(info):
    formatted_info = ''
    for item in info:
        formatted_info += f"{item['title']}\n\n{item['content']}\n\n"
    return formatted_info
