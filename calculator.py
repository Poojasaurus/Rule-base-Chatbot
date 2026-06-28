class Calculator:

    @staticmethod
    def start():

        print("\n" + "=" * 50)
        print("🧮 DecodeBot Calculator")
        print("=" * 50)
        print("Format : number operator number")
        print("Example: 10 + 20")
        print("Supported Operators : +  -  *  /")
        print("Type 'back' to return.\n")

        while True:

            expression = input("Calc > ").strip()

            if expression.lower() == "back":
                print("Leaving Calculator...\n")
                break

            parts = expression.split()

            if len(parts) != 3:
                print("❌ Invalid format.")
                continue

            first, operator, second = parts

            try:
                first = float(first)
                second = float(second)

            except ValueError:

                print("❌ Enter valid numbers.")
                continue

            if operator == "+":
                result = first + second

            elif operator == "-":
                result = first - second

            elif operator == "*":
                result = first * second

            elif operator == "/":

                if second == 0:
                    print("❌ Cannot divide by zero.")
                    continue

                result = first / second

            else:

                print("❌ Invalid operator.")
                continue

            if result.is_integer():
                result = int(result)

            print(f"✅ Result : {result}\n")