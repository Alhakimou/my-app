import speech_recognition as sr
from googletrans import Translator

recognizer = sr.Recognizer()
translator = Translator()

print("🎤 Le programme écoute en continu… Parlez en ANGLAIS.")
print("🛑 Pour arrêter : Ctrl + C\n")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)  # adapte au bruit

    while True:  # boucle infinie
        try:
            print("👉 Parlez…")
            audio = recognizer.listen(source)

            # Reconnaissance anglaise
            text_en = recognizer.recognize_google(audio, language="en-US")
            print("\n🗣️ Anglais :", text_en)

            # Traduction en français
            text_fr = translator.translate(text_en, src="en", dest="fr").text
            print("➡️ Français :", text_fr, "\n")

        except sr.UnknownValueError:
            print("❌ Je n'ai pas compris. Parlez plus clairement…\n")

        except Exception as e:
            print("Erreur :", e)
