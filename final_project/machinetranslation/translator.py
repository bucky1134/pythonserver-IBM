"""
For translation of language
"""
from deep_translator import MyMemoryTranslator

def englis_to_french(english_text):
    """
    Translate the text from english to french
    """
    french_text=MyMemoryTranslator(source="en",target="fr").translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translate the text from french to english
    """
    english_text=MyMemoryTranslator(source="fr",target="en").translate(french_text)
    return english_text
