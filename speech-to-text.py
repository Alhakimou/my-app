import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Parlez maintenant...")
    audio = r.listen(source)
    texte = r.recognize_google(audio, language="fr-FR")
    print("Vous avez dit :", texte)
