from model import ensure_model, load_spacy_model,analyze_text

def launch_event():
    """Ensure the NLP model is downloaded and loaded at server startup."""
    ensure_model()  # Check if model exists
    load_spacy_model()  # Load the model into cache



if __name__ == "__main__":
    launch_event()
    # Test text
    text = "If you're interested in learning more, we strongly suggest our (3-hour) Intro to Machine Learning course, which will help you fully understand all of the code that we've presented here. You'll also know enough to generate even better predictions!"

    result = analyze_text(text)  # Get the result dictionary

    # Check for errors before accessing values
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        pos_tags = result["pos_tags"]
        word_counts = result["word_frequency"]

        print("Part-of-Speech (POS) tagging results:")
        print(pos_tags)

        print("\nWord Frequency Count:")
        print(word_counts)


