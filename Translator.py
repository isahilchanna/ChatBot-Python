from translator import translator

languages=['fr']

text=input("User: Enter your text to translate")
print(f"Bot: I can translate it to {languages}")
# lang=input("into which Language you wanna translate it to?")


translator1=translator.Translator(from_lang='en', to_lang=languages)
tranlation=translator1.translate(text)
print(f'{tranlation}')

