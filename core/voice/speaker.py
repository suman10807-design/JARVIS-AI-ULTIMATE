
import pyttsx3


class JarvisSpeaker:

    def __init__(self):
        self.engine = pyttsx3.init()

        # Configure speaking speed
        self.engine.setProperty("rate", 165)

        # Configure voice volume
        self.engine.setProperty("volume", 1.0)

        self.set_voice()

    def set_voice(self):
        voices = self.engine.getProperty("voices")

        if voices:
            # Use an available system voice
            self.engine.setProperty(
                "voice",
                voices[0].id
            )

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    speaker = JarvisSpeaker()
    speaker.speak("Hello. I am JARVIS. All systems ready.")
