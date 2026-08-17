def get_number(message):
    while True:
        try:
            number = float(input(message))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def calculator():
    while True:
        print("\n===== Basic Calculator =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("\nChoose an operation (1-5): ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please choose a number from 1 to 5.")
            continue

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == "1":
            result = num1 + num2
            print(f"The result of adding {num1} and {num2} is {result}.")

        elif choice == "2":
            result = num1 - num2
            print(f"The result of subtracting {num2} from {num1} is {result}.")

        elif choice == "3":
            result = num1 * num2
            print(f"The result of multiplying {num1} by {num2} is {result}.")

        elif choice == "4":
            while num2 == 0:
                print("Error: Cannot divide by zero.")
                num2 = get_number("Please enter a non-zero second number: ")

            result = num1 / num2
            print(f"The result of dividing {num1} by {num2} is {result}.")

        while True:
            again = input("\nDo you want to perform another calculation? (yes/no): ").lower()

            if again == "yes":
                break
            elif again == "no":
                print("Thank you for using the calculator!")
                return
            else:
                print("Please enter 'yes' or 'no'.")


calculator()