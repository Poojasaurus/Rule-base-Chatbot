from datetime import datetime


class ChatHistory:

    FILE_NAME = "chat_history.txt"

    @staticmethod
    def save(user_message, bot_message):

        with open(ChatHistory.FILE_NAME, "a", encoding="utf-8") as file:

            file.write("=" * 60 + "\n")
            file.write(datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
            file.write("\n")
            file.write("-" * 60 + "\n")

            file.write(f"You : {user_message}\n")
            file.write(f"Bot : {bot_message}\n")

            file.write("=" * 60 + "\n\n")

    @staticmethod
    def view():

        try:

            with open(ChatHistory.FILE_NAME, "r", encoding="utf-8") as file:

                content = file.read()

                print("\n" + "=" * 60)
                print("📜 CHAT HISTORY")
                print("=" * 60)

                if content.strip():
                    print(content)
                else:
                    print("No chat history available.")

        except FileNotFoundError:

            print("\nNo chat history found.\n")

    @staticmethod
    def clear():

        with open(ChatHistory.FILE_NAME, "w", encoding="utf-8") as file:
            file.write("")

        print("✅ Chat history cleared successfully.")