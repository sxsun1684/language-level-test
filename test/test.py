# import spacy
# from collections import Counter
#
# def analyze_text(text, model_name="en_core_web_sm"):
#     try:
#         nlp = spacy.load(model_name)
#     except OSError:
#         from spacy.cli import download
#         download(model_name)
#         nlp = spacy.load(model_name)
#
#     doc = nlp(text)
#
#     word_freq = Counter()
#     pos_info = []
#
#     for token in doc:
#         if token.is_alpha:
#             word = token.text.lower()
#             word_freq[word] += 1
#             pos_info.append((token.text, token.pos_))
#
#     return {
#         "pos_tags": pos_info,
#         "word_freq": word_freq,
#         "unique_words": sorted(word_freq.keys()),
#         "unique_word_count": len(word_freq)
#     }
#
#
#
# def evaluate_proficiency(text, model_name="en_core_web_sm"):
#     try:
#         nlp = spacy.load(model_name)
#     except OSError:
#         from spacy.cli import download
#         download(model_name)
#         nlp = spacy.load(model_name)
#
#     doc = nlp(text)
#     word_freq = Counter()
#     pos_list = []
#
#     for token in doc:
#         if token.is_alpha:
#             word = token.text.lower()
#             word_freq[word] += 1
#             pos_list.append(token.pos_)
#
#     total_words = sum(word_freq.values())
#
#     common_function_words = {
#         "the", "a", "an", "in", "on", "at", "and", "but", "so", "if", "you", "he", "she", "it", "we", "they",
#         "is", "are", "was", "were", "can", "could", "would", "should", "like", "however"
#     }
#     function_word_count = sum(freq for word, freq in word_freq.items() if word in common_function_words)
#     function_word_ratio = function_word_count / total_words
#
#     pos_counter = Counter(pos_list)
#     pos_ttr = len(pos_counter) / len(pos_list) if pos_list else 0
#
#     basic_vocab = {
#         "good", "bad", "very", "thing", "get", "do", "say", "go", "come",
#         "nice", "people", "man", "woman", "boy", "girl", "have", "be", "eat"
#     }
#     basic_word_count = sum(freq for word, freq in word_freq.items() if word in basic_vocab)
#     basic_word_ratio = basic_word_count / total_words
#
#     return {
#         "total_words": total_words,
#         "unique_words": len(word_freq),
#         "function_word_ratio": round(function_word_ratio, 4),
#         "pos_ttr": round(pos_ttr, 4),
#         "basic_vocab_ratio": round(basic_word_ratio, 4),
#         "function_word_count": function_word_count,
#         "basic_word_count": basic_word_count,
#         "word_freq": word_freq,
#         "pos_distribution": pos_counter
#     }
#
# if __name__ == "__main__":
#     text = open("../text/Yukiko Tominaga.txt", encoding="utf-8").read()
#     result = analyze_text(text)
#     prof = evaluate_proficiency(text)
#
#     print("\n--- Language Proficiency Evaluation ---")
#     print(f"Total Words: {prof['total_words']}")
#     print(f"Unique Words: {prof['unique_words']}")
#     print(f"Function Word Ratio: {prof['function_word_ratio']}")
#     print(f"POS Type-Token Ratio (TTR): {prof['pos_ttr']}")
#     print(f"Basic Vocabulary Usage Ratio: {prof['basic_vocab_ratio']}")
