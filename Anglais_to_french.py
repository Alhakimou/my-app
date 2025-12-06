import speech_recognition as sr
from googletrans import Translator

recognizer = sr.Recognizer()
translator = Translator()

with sr.Microphone() as source:
    print("🎤 Parlez en ANGLAIS...")
    audio = recognizer.listen(source)

try:
    # Reconnaissance de l’anglais
    text_en = recognizer.recognize_google(audio, language="en-US")
    print("Texte détecté (anglais) :", text_en)

    # Traduction anglais → français
    text_fr = translator.translate(text_en, src="en", dest="fr").text
    print("Traduction (français) :", text_fr)

except Exception as e:
    print("Erreur :", e)
