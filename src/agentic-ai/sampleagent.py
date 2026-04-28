from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


class GeminiAgent:
    def __init__(self, model="gemini-3-flash-preview"):
        # Uses GEMINI_API_KEY from environment automatically
        self.client = genai.Client()
        self.model = model
        self.memory = []

    def ask(self, user_input: str) -> str:
        self.memory.append(f"User: {user_input}")

        conversation = "\n".join(self.memory)

        response = self.client.models.generate_content(
            model=self.model,
            contents=(
                "You are a helpful AI assistant.\n"
                "Keep answers clear and short.\n\n"
                f"Conversation so far:\n{conversation}"
            ),
        )

        answer = response.text
        self.memory.append(f"Assistant: {answer}")
        return answer

    def chat(self):
        print("Gemini Agent: Hello! Type 'exit' to stop.")

        while True:
            user_input = input("You: ").strip()

            if user_input.lower() == "exit":
                print("Gemini Agent: Goodbye!")
                break

            try:
                reply = self.ask(user_input)
                print("Gemini Agent:", reply)
            except Exception as e:
                print("Error:", e)


if __name__ == "__main__":
    if not os.getenv("GEMINI_API_KEY"):
        print("GEMINI_API_KEY is not set.")
    else:
        agent = GeminiAgent()
        agent.chat()