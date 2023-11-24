import speech_recognition as sr
import pyttsx3

def escuchar():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            return recognizer.recognize_google(audio, language='es-ES')
        except sr.UnknownValueError:
            return "No se pudo entender el audio"
        except sr.RequestError as e:
            return f"Error en la solicitud a Google Speech Recognition: {e}"

def hablar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

if __name__ == "__main__":
    hablar("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte?")

    while True:
        comando = escuchar().lower()

        if "detener" in comando:
            hablar("Hasta luego")
            break
        else:
            hablar("Lo siento, no entendí el comando. ¿Puedes repetirlo?")
