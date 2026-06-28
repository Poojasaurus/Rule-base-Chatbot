from utils import Utils


class Banner:

    @staticmethod
    def show():

        Utils.title("🤖 DecodeBot Pro v1.0")

        print("Professional Rule-Based AI Chatbot")
        print("Built with Python\n")

        print("Available Commands")
        print("-" * 25)

        commands = [
            "hi / hello / hey",
            "good morning",
            "good afternoon",
            "good evening",
            "how are you",
            "what is your name",
            "who made you",
            "python",
            "ai",
            "machine learning",
            "time",
            "date",
            "calculator",
            "history",
            "clear history",
            "help",
            "about",
            "version",
            "joke",
            "motivate me",
            "exit"
        ]

        for command in commands:
            print(f"✔ {command}")

        print("\nType 'help' anytime to see the commands again.")
        print(Utils.line())