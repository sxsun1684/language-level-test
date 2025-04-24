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
    """提取每个唯一单词的词性和频率（小写、去重）"""
    if MODEL_CACHE is None:
        load_spacy_model()
    if MODEL_CACHE is None:
        return {"error": "Model not loaded"}

    doc = MODEL_CACHE(text)

    word_freq = Counter()
    word_pos_map = {}

    for token in doc:
        if token.is_alpha:
            word_lower = token.text.lower()
            word_freq[word_lower] += 1
            # 只记录第一次遇到的词性
            if word_lower not in word_pos_map:
                word_pos_map[word_lower] = token.pos_

    return {
        "word_pos_freq": {word: {"pos": word_pos_map[word], "freq": freq}
            for word, freq in word_freq.items()},
        "unique_word_count": len(word_freq)
    }
