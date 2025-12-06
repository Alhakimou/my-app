import speech_recognition as sr
from googletrans import Translator

recognizer = sr.Recognizer()
translator = Translator()

print("🎤 Le programme écoute en continu… Parlez en FRANÇAIS.")
print("🛑 Pour arrêter : Ctrl + C\n")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)

    while True:
        try:
            print("👉 Parlez…")
            audio = recognizer.listen(source)

            # Reconnaissance du français
            text_fr = recognizer.recognize_google(audio, language="fr-FR")
            print("\n🗣️ Français :", text_fr)

            # Traduction français → anglais
            text_en = translator.translate(text_fr, src="fr", dest="en").text
            print("➡️ English :", text_en, "\n")

        except sr.UnknownValueError:
            print("❌ Je n’ai pas compris. Répétez svp…\n")

        except Exception as e:
            print("Erreur :", e)
