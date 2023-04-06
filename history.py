import os

HISTORY_FILE = 'history.txt'

def read_history():
    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'w') as f:
            f.write('')
    with open(HISTORY_FILE, 'r') as f:
        history = f.read()
    return history

def add_to_history(user_input, response):
    with open(HISTORY_FILE, 'a') as f:
        f.write(f'User: {user_input}\nGLAM: {response}\n\n')

def write_history(user_input, response):
    with open(HISTORY_FILE, 'a') as f:
        f.write(f'User: {user_input}\nGLAM: {response}\n\n')

    # Add the same text to a separate file for easier parsing
    with open('history_parsed.txt', 'a') as f:
        f.write(f'{user_input}\t{response}\n')
