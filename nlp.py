import spacy

nlp = spacy.load("en_core_web_sm")

def process_symptoms(symptoms: str):
    """
    Process user-entered symptoms using NLP.
    """
    doc = nlp(symptoms)
    processed = " ".join([token.lemma_ for token in doc if not token.is_stop])
    return processed
