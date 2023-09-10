import random
from nltk.corpus import wordnet
import re

def ai_similarise(message):
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
        # Split the sentence into clauses and vary their order
        clauses = text.split(',')
        random.shuffle(clauses)
        return ', '.join(clauses)

    message = message.lower()  # Convert to lowercase for consistency
    message = replace_words(message)
    message = vary_sentence_structure(message)

    return message

# Example usage:
original_message = "Sorry, you lost the game!"
similar_message = ai_similarise(original_message)
print(similar_message)
