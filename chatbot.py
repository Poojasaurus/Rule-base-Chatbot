
import random
import time
from datetime import datetime

from colorama import Fore, Style, init

init(autoreset=True)

class DecodeBot:

    def __init__(self):

        self.name = "DecodeBot Pro"
        self.version = "2.0"
        self.running = True

        self.responses = {
            "greetings": [
                "Hello! 👋",
                "Hi there!",
                "Hey! Nice to see you.",
                "Welcome! 😊"
            ],

            "how_are_you": [
                "I'm doing great!",
                "Fantastic!",
                "I'm always ready to help."
            ],

            "name": [
                "I'm DecodeBot Pro."
            ],

            "creator": [
                "I was built using Python."
            ],

            "python": [
                "Python is one of the most popular programming languages."
            ],

            "ai": [
                "Artificial Intelligence enables machines to think intelligently."
            ],

            "ml": [
                "Machine Learning is a branch of AI."
            ],

            "thanks": [
                "You're welcome!",
                "Happy to help!",
                "Anytime 😊"
            ],

            "jokes": [
                "Why do programmers prefer dark mode? Because light attracts bugs! 😂",
                "Debugging is like being the detective and the criminal at the same time. 😄"
            ],

            "motivation": [
                "Success is built one day at a time.",
                "Keep learning. You're improving every day."
            ]
        }

    def line(self):
        return "=" * 65

    def typing(self):

        print("\n🤖 DecodeBot", end="", flush=True)

        for _ in range(3):
            time.sleep(0.4)
            print(".", end="", flush=True)

        print()

    def bot(self, message):

        self.typing()

        print(Fore.GREEN + f"🤖 {message}" + Style.RESET_ALL)

    def banner(self):

        print(Fore.CYAN + "\n" + self.line())
        print(Fore.CYAN + "        🤖 DecodeBot Pro v2.0")
        print(Fore.CYAN + self.line())

        print(Fore.YELLOW + "Professional Rule-Based AI Chatbot\n")

        print(Fore.WHITE + "Started : " +
          datetime.now().strftime("%d %B %Y %I:%M %p"))

        print(Fore.CYAN + self.line())

        self.bot("Hello! Type 'help' to see available commands.")

    def help(self):

        print("\n" + self.line())
        print("AVAILABLE COMMANDS")
        print(self.line())

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
            "joke",
            "motivate me",
            "about",
            "version",
            "help",
            "exit"
        ]

        for command in commands:
            print("✔", command)

        print(self.line())

    def about(self):

        print("\n" + self.line())
        print("ABOUT")
        print(self.line())

        print(f"Project  : {self.name}")
        print(f"Version  : {self.version}")
        print("Language : Python")
        print("Type     : Rule-Based AI Chatbot")
        print("Author   : DecodeLabs Internship Project")

        print(self.line())

    def current_time(self):

        return datetime.now().strftime("%I:%M:%S %p")

    def current_date(self):

        return datetime.now().strftime("%d %B %Y")

    def save_history(self, user, bot):

        with open("chat_history.txt", "a", encoding="utf-8") as file:

            file.write("=" * 60 + "\n")
            file.write(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
            file.write("\n")
            file.write(f"You : {user}\n")
            file.write(f"Bot : {bot}\n")
            file.write("=" * 60 + "\n\n")

    def view_history(self):

        try:

            with open("chat_history.txt", "r", encoding="utf-8") as file:

                print("\n" + self.line())
                print("CHAT HISTORY")
                print(self.line())

                content = file.read()

                if content.strip():
                    print(content)
                else:
                    print("No chat history available.")

        except FileNotFoundError:

            print("\nNo chat history found.")

    def clear_history(self):

        with open("chat_history.txt", "w", encoding="utf-8") as file:
            file.write("")

        self.bot("Chat history cleared successfully.")

    def calculator(self):

        print("\n" + self.line())
        print("CALCULATOR")
        print(self.line())

        print("Example : 10 + 20")
        print("Type 'back' to return.\n")

        while True:

            expression = input("Calc > ").strip()

            if expression.lower() == "back":
                break

            parts = expression.split()

            if len(parts) != 3:
                print(Fore.RED + "❌ Invalid format." + Style.RESET_ALL)
                continue

            first, operator, second = parts

            try:

                first = float(first)
                second = float(second)

            except ValueError:
                print(Fore.RED + "❌ Invalid numbers." + Style.RESET_ALL)
                continue

            if operator == "+":
                result = first + second

            elif operator == "-":
                result = first - second

            elif operator == "*":
                result = first * second

            elif operator == "/":

                if second == 0:
                    print(Fore.RED + "❌ Cannot divide by zero." + Style.RESET_ALL)
                    continue

                result = first / second

            else:
                print(Fore.RED + "❌ Invalid operator." + Style.RESET_ALL)
                continue

            if result.is_integer():
                result = int(result)

            print("Result :", result)

    def get_response(self, user):

        user = user.lower()

        if any(word in user for word in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]):
            return random.choice(self.responses["greetings"])

        elif "how are you" in user:
            return random.choice(self.responses["how_are_you"])

        elif "your name" in user or "who are you" in user:
            return random.choice(self.responses["name"])

        elif "who made you" in user or "who created you" in user:
            return random.choice(self.responses["creator"])

        elif "python" in user:
            return random.choice(self.responses["python"])

        elif "artificial intelligence" in user or user == "ai":
            return random.choice(self.responses["ai"])

        elif "machine learning" in user or user == "ml":
            return random.choice(self.responses["ml"])

        elif "joke" in user:
            return random.choice(self.responses["jokes"])

        elif "motivate" in user:
            return random.choice(self.responses["motivation"])

        elif "thank" in user:
            return random.choice(self.responses["thanks"])

        return "Sorry, I don't understand that. Type 'help' to see available commands."

    def execute(self, user):

        if user == "help":
            self.help()
            return

        elif user == "about":
            self.about()
            return

        elif user == "version":
            self.bot(f"Current Version : {self.version}")
            return

        elif user == "time":
            self.bot(f"Current Time : {self.current_time()}")
            return

        elif user == "date":
            self.bot(f"Today's Date : {self.current_date()}")
            return

        elif user == "calculator":
            self.calculator()
            return

        elif user == "history":
            self.view_history()
            return

        elif user == "clear history":
            self.clear_history()
            return

        response = self.get_response(user)

        self.bot(response)

        self.save_history(user, response)

    def run(self):

        self.banner()

        while self.running:

            try:

                user = input(
                    Fore.BLUE + "\n👤 You : " + Style.RESET_ALL
                ).strip().lower()

                if user == "":
                    print("⚠ Please enter a message.")
                    continue

                if user in ["exit", "quit", "bye"]:

                    self.bot("Goodbye! 👋 Thanks for using DecodeBot Pro.")

                    self.save_history(user, "Session Ended")

                    self.running = False

                    break

                self.execute(user)

            except KeyboardInterrupt:

                print()

                self.bot("Session interrupted. Goodbye!")

                break

            except Exception as error:

                print(f"\n❌ Error : {error}")


def main():
    chatbot = DecodeBot()
    chatbot.run()


if __name__ == "__main__":
    main()