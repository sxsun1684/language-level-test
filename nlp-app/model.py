import spacy
from spacy.cli import download
from collections import Counter

from config import MODEL_NAME, MODEL_CACHE

def ensure_model():
    """Ensure the spaCy language model is installed."""
    try:
        if MODEL_NAME not in spacy.util.get_installed_models():
            print(f"Model '{MODEL_NAME}' not found. Downloading now...")
            download(MODEL_NAME)  # Download if missing
    except Exception as e:
        print(f"Error ensuring model '{MODEL_NAME}': {e}")

def load_spacy_model():
    """Load and cache the spaCy language model."""
    global MODEL_CACHE  # Use the global variable from config.py
    if MODEL_CACHE is None:
        try:
            MODEL_CACHE = spacy.load(MODEL_NAME)  # Load the spaCy model
            print(f"Model '{MODEL_NAME}' loaded successfully.")
        except Exception as e:
            print(f"Error loading spaCy model '{MODEL_NAME}': {e}")
            MODEL_CACHE = None  # Ensure it remains None if loading fails

def analyze_text(text):
    """Process text: extract POS tagging and word frequency."""
    if MODEL_CACHE is None:
        load_spacy_model()  # Attempt to load the model if not loaded

    if MODEL_CACHE is None:
        return {"error": "Model not loaded"}  #This means MODEL_CACHE was never initialized!

    doc = MODEL_CACHE(text)
    word_freq = Counter()
    pos_info = []

    for token in doc:
        if token.is_alpha:
            word_freq[token.text.lower()] += 1
            pos_info.append((token.text, token.pos_))

    return {"pos_tags": pos_info, "word_frequency": word_freq}



