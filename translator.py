from deep_translator import GoogleTranslator

print("=== Language Translation Tool ===")

text = input("Enter text to translate: ")

translated = GoogleTranslator(
    source='auto',
    target='ta'
).translate(text)

print("\nTranslated Text:")
print(translated)
