from googletrans import Translator
from indicnlp.tokenize import indic_tokenize

# Function to translate English text to Tamil and tokenize it
def translate_and_tokenize(text):
    # Initialize translator
    translator = Translator()

    # Translate text from English to Tamil
    translation = translator.translate(text, src='en', dest='ta')

    # Get translated Tamil text
    tamil_text = translation.text

    # Tokenize the translated Tamil text
    tokens = indic_tokenize.trivial_tokenize(tamil_text)

    return tokens

# English text to be translated
english_text = "what is my name."

# Translate English text to Tamil and tokenize it
tamil_tokens = translate_and_tokenize(english_text)

# Printing the tokens
print("Tokens in Tamil:")
for token in tamil_tokens:
    print(token)