
import os
from dotenv import load_dotenv

from core.ai_brain import JarvisBrain
from voice.speaker import JarvisSpeaker
from voice.listener import JarvisListener
from desktop.controller import JarvisController


load_dotenv()


class Jarvis:

    def __init__(self):
        print("Initializing JARVIS...")

        self.brain = JarvisBrain()
        self.speaker = JarvisSpeaker()
        self.listener = JarvisListener()
        self.controller = JarvisController()

        print("All systems initialized.")

    def run(self):

        self.speaker.speak(
            "Hello. I am JARVIS. How may I help you?"
        )

        while True:

            question = self.listener.listen()

            if not question:
                continue

            command = question.lower().strip()

            if command in ["exit", "quit", "shutdown jarvis"]:
                self.speaker.speak(
                    "Goodbye. JARVIS shutting down."
                )
                break

            if command == "open notepad":
                result = self.controller.open_application(
                    "notepad"
                )
                print("JARVIS:", result)
                self.speaker.speak(result)
                continue

            print("JARVIS is thinking...")

            answer = self.brain.ask(question)

            print("\nJARVIS:", answer)

            self.speaker.speak(answer)


if __name__ == "__main__":

    try:
        jarvis = Jarvis()
        jarvis.run()

    except KeyboardInterrupt:
        print("\nJARVIS stopped.")

    except Exception as error:
        print("JARVIS startup error:", error)
