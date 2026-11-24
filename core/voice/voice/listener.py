
import speech_recognition as sr


class JarvisListener:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.recognizer.dynamic_energy_threshold = True

    def listen(self):

        try:
            with sr.Microphone() as source:

                print("JARVIS: Listening...")

                self.recognizer.adjust_for_ambient_noise(
                    source, duration=0.5
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=15
                )

            print("JARVIS: Understanding...")

            text = self.recognizer.recognize_google(audio)

            print("You:", text)

            return text

        except sr.WaitTimeoutError:
            print("JARVIS: No speech detected.")
            return None

        except sr.UnknownValueError:
            print("JARVIS: I couldn't understand that.")
            return None

        except sr.RequestError:
            print("JARVIS: Speech recognition service unavailable.")
            return None

        except OSError:
            print("JARVIS: Microphone not available.")
            return None


if __name__ == "__main__":
    listener = JarvisListener()
    listener.listen()
