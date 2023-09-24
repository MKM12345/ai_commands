import random
from nltk.corpus import wordnet
import re
from textblob import TextBlob

def ai_similarise(message):
    """
    If you want a different wording to an output when a specific condition is met and gives an output, this will make things a little less boring!

    It generates similar but varied text for a given input message using synonyms and sentence structure variation.

    This function takes an input message and applies two main techniques to generate similar yet different text:
    1. Synonym Replacement: It replaces words in the message with synonyms when synonyms are available. This adds lexical variation to the text.
    2. Sentence Structure Variation: It shuffles the clauses in the sentence to change its structure and provide additional variation.

    Warnings:
    - The function uses NLTK's WordNet corpus for synonym replacement, which may not always provide the most contextually accurate synonyms.
    - While efforts have been made to maintain sentence coherence, generated text may occasionally be grammatically incorrect or nonsensical.
    - The quality of generated variations depends on the availability of synonyms and sentence structure possibilities for the input message.

    Parameters:
    message (str): The input message for which similar text variations are generated.

    Returns:
    str: A text variation of the input message with synonyms and sentence structure changes.
    """
    def synonym_replacement(word):
        synonyms = wordnet.synsets(word)
        if synonyms:
            synonym = random.choice(synonyms).lemmas()[0].name()
            return synonym
        return word

    def replace_words(text):
        words = re.findall(r'\w+', text)
        new_words = [synonym_replacement(word) for word in words]
        return ' '.join(new_words)

    def vary_sentence_structure(text):
        # Split the sentence into clauses based on punctuation
        clauses = re.split(r'([.,!?])', text)
        clauses = [clause.strip() for clause in clauses if clause.strip()]

        # Shuffle and reassemble the clauses
        random.shuffle(clauses)
        return ''.join(clauses)

    message = message.lower()  # Convert to lowercase for consistency
    message = replace_words(message)
    message = vary_sentence_structure(message)

    return message

def analyze_sentiment(text):
    """
    Analyze the sentiment of a text using Natural Language Processing (NLP).

    Parameters:
    text (str): The input text to be analyzed.

    Returns:
    dict: A dictionary containing the sentiment label, sentiment score, and a sentiment summary.
    """
    analysis = TextBlob(text)
    sentiment_score = analysis.sentiment.polarity

    if sentiment_score > 0:
        sentiment_label = "positive"
        sentiment_summary = "This text expresses a positive sentiment."
    elif sentiment_score < 0:
        sentiment_label = "negative"
        sentiment_summary = "This text expresses a negative sentiment."
    else:
        sentiment_label = "neutral"
        sentiment_summary = "This text appears to be neutral in sentiment."

    result = {
        "sentiment_label": sentiment_label,
        "sentiment_score": sentiment_score,
        "sentiment_summary": sentiment_summary
    }

    return result
