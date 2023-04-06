import transformers
from transformers import AutoModelForTokenClassification, AutoTokenizer
import torch

# define the model and tokenizer paths
MODEL = "./glam/greek_legal_bert_v2-finetuned-ner"
TOKENIZER = "./glam/greek_legal_bert_v2-finetuned-ner"

# load the model and tokenizer
NER_MODEL = AutoModelForTokenClassification.from_pretrained(MODEL)
NER_TOKENIZER = AutoTokenizer.from_pretrained(TOKENIZER)

# define the labels for the named entities
LABELS = [
    "O",  # Outside of a named entity
    "B-PER",  # Beginning of a person's name
    "I-PER",  # Middle of a person's name
    "B-ORG",  # Beginning of an organization
    "I-ORG",  # Middle of an organization
    "B-LOC",  # Beginning of a location
    "I-LOC",  # Middle of a location
    "B-LEG",  # Beginning of a legal entity
    "I-LEG",  # Middle of a legal entity
]

# set the device to use
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# define the function to get named entities
def get_named_entities(text):
    # tokenize the text
    tokens = NER_TOKENIZER.encode(text, add_special_tokens=False)

    # convert token ids to tensor
    token_ids = torch.tensor(tokens).unsqueeze(0).to(DEVICE)

    # get the model's predictions
    with torch.no_grad():
        predictions = NER_MODEL(token_ids)[0][0]

    # convert prediction indices to labels
    labels = [LABELS[prediction.argmax().item()] for prediction in predictions]

    # extract named entities
    named_entities = []
    current_entity = None
    for token, label in zip(NER_TOKENIZER.tokenize(text), labels):
        if label.startswith("B-"):
            if current_entity:
                named_entities.append(current_entity)
            current_entity = {"entity": token, "type": label[2:]}
        elif label.startswith("I-"):
            if current_entity and current_entity["type"] == label[2:]:
                current_entity["entity"] += token.replace("▁", " ")
            else:
                if current_entity:
                    named_entities.append(current_entity)
                current_entity = None
        else:
            if current_entity:
                named_entities.append(current_entity)
            current_entity = None

    if current_entity:
        named_entities.append(current_entity)

    return named_entities
