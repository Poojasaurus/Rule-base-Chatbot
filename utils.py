from datetime import datetime


class Utils:

    @staticmethod
    def current_time():
        return datetime.now().strftime("%I:%M:%S %p")

    @staticmethod
    def current_date():
        return datetime.now().strftime("%d %B %Y")

    @staticmethod
    def current_datetime():
        return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    @staticmethod
    def line(length=70):
        return "=" * length

    @staticmethod
    def title(text):

        print("\n" + Utils.line())
        print(text.center(70))
        print(Utils.line())

    @staticmethod
    def pause():

        input("\nPress Enter to continue...")