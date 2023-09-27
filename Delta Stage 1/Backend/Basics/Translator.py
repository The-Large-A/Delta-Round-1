#Translator

from googletrans import Translator, LANGUAGES, LANGCODES
translator = Translator()

while True:
    try:
        choice = int(input("Select Mode: \n1-Translate to English \n2-Detect Language \n3-Manual Translate \n4-Quit \n"))

        if choice == 1:
            text = input("Enter text to be translated to English: ")
            source = input("Enter code of Source Lang: ")
            try:
                translated_text = translator.translate(text, src=source, dest='en')
                print(f"Translation ({LANGUAGES[source]} to English): {translated_text.text}")
            except Exception as e:
                print("Translation failed. Please check your input.")
        
        elif choice == 3:
            text = input("Enter text to be translated to: ")
            source = input("Enter code of Source Lang: ")
            target = input("Enter code of Destination Language: ")
            try:
                translated_text = translator.translate(text, src=source, dest=target)
                print(f"Translation ({LANGUAGES[source]} to {LANGUAGES[target]}): {translated_text.text}")
            except Exception as e:
                print("Translation failed. Please check your input.")
        
        elif choice == 2:
            text = input("Enter text to detect language of: ")
            detected_language = translator.detect(text)
            print(f"Detected Language: {LANGUAGES[detected_language.lang]}")
        
        elif choice == 4:
            print("Quitting Application")
            break
        
        else:
            print("Invalid, enter a valid choice")

    except TypeError:
        print("Invalid, enter a valid choice")