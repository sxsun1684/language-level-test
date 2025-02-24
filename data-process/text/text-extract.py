import spacy
from spacy.cli import download
from collections import Counter

# Global cache to store loaded models, avoiding redundant loads
MODEL_CACHE = {}


def ensure_model(model_name):
    """Ensure that the spaCy language model is installed.

    If the model is not found, attempt to download it.
    Handles exceptions to prevent crashes in case of errors.
    """
    try:
        if model_name not in spacy.util.get_installed_models():
            print(f"Model '{model_name}' not found. Downloading it now...")
            download(model_name)  # Download the model if not installed
    except Exception as e:
        print(f"Error ensuring model '{model_name}': {e}")


def load_spacy_model(model_name):
    """Load the spaCy language model and cache it for reuse.

    This prevents repeated loading of the model, optimizing performance for high-concurrency use cases.
    """
    if model_name in MODEL_CACHE:
        return MODEL_CACHE[model_name]  # Return cached model if available

    try:
        nlp = spacy.load(model_name)  # Load spaCy model
        MODEL_CACHE[model_name] = nlp  # Store it in cache
        return nlp
    except Exception as e:
        print(f"Error loading spaCy model '{model_name}': {e}")
        return None  # Return None if model loading fails


def get_word_pos_freq(text):
    """Extract word frequencies and part-of-speech (POS) tags from the given text.

    Ensures the language model is available, loads it efficiently, and processes the text.
    Returns a list of words with their POS tags and a frequency count of words.
    """
    ensure_model("en_core_web_sm")  # Ensure model is installed
    nlp = load_spacy_model("en_core_web_sm")  # Load and cache the model

    if not nlp:  # If model loading fails, return empty results
        return [], Counter()

    doc = nlp(text)  # Process the text
    word_freq = Counter()  # Counter for word frequency
    pos_info = []  # Store (word, POS) pairs

    for token in doc:
        if token.is_alpha:  # Only consider alphabetic words (ignore punctuation)
            word_freq[token.text.lower()] += 1  # Count word occurrences
            pos_info.append((token.text, token.pos_))  # Store word with POS

    return pos_info, word_freq


# Test text
text = "She runs quickly and speaks fluently. The beautiful sky is amazing. She runs fast and speaks clearly."

pos_tags, word_counts = get_word_pos_freq(text)

print("Part-of-Speech (POS) tagging results:")
print(pos_tags)  # Output list of (word, POS) tuples

print("\nWord Frequency Count:")
print(word_counts)  # Output word frequency dictionary
