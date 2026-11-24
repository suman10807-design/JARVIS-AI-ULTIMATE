
import os
from openai import OpenAI


class JarvisBrain:

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OpenAI API key is missing.")

        self.client = OpenAI(api_key=api_key)
        self.model = os.getenv("JARVIS_MODEL", "gpt-6.2-astra")

        self.history = []

        self.instructions = """
        You are JARVIS, an advanced personal AI assistant.

        Your abilities:
        1. Answer general knowledge questions.
        2. Solve mathematics step by step.
        3. Explain science and other subjects.
        4. Write and debug programming code.
        5. Help with research and learning.
        6. Have natural conversations.

        Always give accurate, clear and helpful answers.
        Explain difficult concepts in simple language.
        """

    def ask(self, question):

        self.history.append({
            "role": "user",
            "content": question
        })

        try:
            response = self.client.responses.create(
                model=self.model,
                instructions=self.instructions,
                input=self.history[-12:]
            )

            answer = response.output_text

            self.history.append({
                "role": "assistant",
                "content": answer
            })

            return answer

        except Exception as error:
            self.history.pop()
            return f"JARVIS Error: {error}"
