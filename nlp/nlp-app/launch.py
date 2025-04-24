from model import ensure_model, load_spacy_model,analyze_text

def launch_event():
    """Ensure the NLP model is downloaded and loaded at server startup."""
    ensure_model()  # Check if model exists
    load_spacy_model()  # Load the model into cache



if __name__ == "__main__":
    launch_event()
    ensure_model()

    file_path = "../../text/Yukiko Tominaga.txt"
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        exit()

    result = analyze_text(text)

    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"\n--- Unique Words with POS and Frequency (Total: {result['unique_word_count']}) ---")
        for word, info in sorted(result["word_pos_freq"].items()):
            print(f"{word} -> POS: {info['pos']}, Frequency: {info['freq']}")
